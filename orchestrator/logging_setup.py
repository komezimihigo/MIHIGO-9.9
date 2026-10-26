import json, logging, sys
from datetime import datetime, timezone
class Formatter(logging.Formatter):
 def format(self, record):
    d={"ts":datetime.now(timezone.utc).isoformat(),"level":record.levelname,
       "logger":record.name,"message":record.getMessage()}
    for k in ("event","job_id","stage","attempt","provider","channel_id"):
        if hasattr(record,k): d[k]=getattr(record,k)
    if record.exc_info: d["traceback"]=self.formatException(record.exc_info)
    return json.dumps(d,ensure_ascii=False)
def configure():
 h=logging.StreamHandler(sys.stdout); h.setFormatter(Formatter())
 root=logging.getLogger(); root.handlers.clear(); root.addHandler(h); root.setLevel("INFO")
 logging.getLogger("mihigo").info("LOGGING_INITIALIZED",extra={"event":"startup"})
 return logging.getLogger("mihigo")
