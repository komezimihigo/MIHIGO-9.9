import logging
log=logging.getLogger("mihigo.youtube")
def publish_video(job,mp4_path,channel):
 log.info("PUBLISH_START job_id=%s channel_id=%s privacy=%s",job.get("job_id"),channel.get("channel_id"),channel.get("privacy_status","private"))
 raise NotImplementedError("OAuth, resumable uploader, reconciliation and video-ID persistence must be configured.")
