import os,logging,traceback
from flask import Flask,request,jsonify
logging.basicConfig(level=logging.INFO,format="%(asctime)s %(levelname)s %(message)s")
log=logging.getLogger("mihigo.cloudrun");app=Flask(__name__)
@app.get("/health")
def health(): log.info("HEALTHCHECK_OK");return jsonify(ok=True,version="9.8")
@app.post("/jobs")
def jobs():
 token=os.getenv("INTERNAL_API_TOKEN","")
 if not token or request.headers.get("Authorization")!="Bearer "+token: log.warning("UNAUTHORIZED");return jsonify(ok=False,error="unauthorized"),401
 body=request.get_json(silent=True) or {}; jid=body.get("job_id")
 if not jid:return jsonify(ok=False,error="job_id required"),400
 log.info("JOB_RECEIVED id=%s format=%s",jid,body.get("output_format"))
 try: raise NotImplementedError("Connect R2, rights gate, renderer and durable status reporting before use.")
 except Exception as e: log.error("JOB_FAILED id=%s error=%s\n%s",jid,e,traceback.format_exc());return jsonify(ok=False,error="worker not fully configured"),501
if __name__=="__main__":app.run(host="0.0.0.0",port=int(os.getenv("PORT","8080")))
