const now=()=>new Date().toISOString();
const out=(x,status=200)=>new Response(JSON.stringify(x,null,2),{status,headers:{"content-type":"application/json"}});
const log=(level,event,details={})=>console.log(JSON.stringify({ts:now(),service:"mihigo-cloudflare",level,event,...details}));
async function authorized(req,env){return !!env.INTERNAL_API_TOKEN && req.headers.get("authorization")==="Bearer "+env.INTERNAL_API_TOKEN;}
export default {
 async fetch(req,env){
  const u=new URL(req.url); log("INFO","request_received",{method:req.method,path:u.pathname});
  if(u.pathname==="/health") return out({ok:true,version:"9.8",time:now()});
  if(!await authorized(req,env)) return out({ok:false,error:"Unauthorized"},401);
  if(u.pathname==="/api/jobs" && req.method==="POST"){
   let b; try{b=await req.json()}catch(e){log("ERROR","invalid_json",{error:String(e)});return out({ok:false,error:"Invalid JSON"},400)}
   if(!b.source_url||!b.source_kind)return out({ok:false,error:"source_url and source_kind required"},400);
   const id=b.job_id||crypto.randomUUID(), t=now(), fmt=b.output_format==="standard"?"standard":"short";
   try{
    await env.DB.prepare("INSERT INTO jobs(job_id,source_url,source_kind,state,output_format,channel_id,source_license,license_url,creator,attribution,rights_evidence,created_at,updated_at) VALUES(?,?,?,'DISCOVERED',?,?,?,?,?,?,?,?,?)")
    .bind(id,b.source_url,b.source_kind,fmt,b.channel_id||"",b.source_license||"",b.license_url||"",b.creator||"",b.attribution||"",b.rights_evidence||"",t,t).run();
    await env.DB.prepare("INSERT INTO events(job_id,level,event,message,created_at) VALUES(?,'INFO','job_created','Job queued',?)").bind(id,t).run();
    log("INFO","job_created",{job_id:id,format:fmt});return out({ok:true,job_id:id,state:"DISCOVERED",note:"Queued; processing worker must be configured."},201);
   }catch(e){log("ERROR","job_create_failed",{job_id:id,error:String(e),stack:e?.stack});return out({ok:false,error:"DB write failed",job_id:id},500)}
  }
  if(u.pathname.startsWith("/api/jobs/")&&req.method==="GET"){
   const id=u.pathname.split("/").pop(), row=await env.DB.prepare("SELECT * FROM jobs WHERE job_id=?").bind(id).first();
   return row?out({ok:true,job:row}):out({ok:false,error:"Not found"},404);
  }
  if(u.pathname==="/api/summary"){
   const r=await env.DB.prepare("SELECT state,COUNT(*) AS count FROM jobs GROUP BY state").all();return out({ok:true,counts:r.results||[]});
  }
  return out({ok:false,error:"Not found"},404);
 },
 async scheduled(controller,env){
  log("INFO","cron_started",{scheduledTime:controller.scheduledTime});
  try{
   const r=await env.DB.prepare("SELECT job_id,state FROM jobs WHERE state IN ('DISCOVERED','READY','RETRY_WAIT','READY_TO_PUBLISH') ORDER BY created_at LIMIT 50").all();
   log("INFO","dispatch_scan",{count:r.results?.length||0,note:"Provider dispatch adapter must be connected."});
  }catch(e){log("ERROR","cron_failed",{error:String(e),stack:e?.stack})}
 }
};
