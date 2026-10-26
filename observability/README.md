# Logs and email alerts
Hosted platforms capture stdout/stderr. Emit timestamped structured logs for STARTUP, CONFIG_MISSING, JOB_CREATED, JOB_CLAIMED, RIGHTS_REJECTED, PROCESS_START, PROCESS_DONE, VALIDATION_FAILED, PUBLISH_START, PUBLISH_DONE, RETRY_SCHEDULED, WORKER_CRASH, QUOTA_EXHAUSTED, WATCHDOG_RECOVERY and EMAIL_FAILED.
SMTP helper uses STARTTLS. Configure a verified sender and dedicated app password/transactional email credentials. Test alerts deliberately. Avoid email storms and never include secrets, access tokens or signed URLs in messages.
