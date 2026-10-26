import os, logging, smtplib, ssl
from email.message import EmailMessage
log = logging.getLogger("mihigo.alerts")

def send_email(subject, body):
    required = ("ALERT_EMAIL_TO", "ALERT_EMAIL_FROM", "SMTP_HOST", "SMTP_PORT", "SMTP_USERNAME", "SMTP_PASSWORD")
    missing = [k for k in required if not os.getenv(k)]
    if missing:
        log.error("EMAIL_NOT_SENT missing_config=%s", ",".join(missing),
                  extra={"event": "email_config_missing", "stage": "alerts"})
        return False
    message = EmailMessage()
    message["Subject"] = "[MIHIGO 9.8] " + subject
    message["From"] = os.environ["ALERT_EMAIL_FROM"]
    message["To"] = os.environ["ALERT_EMAIL_TO"]
    message.set_content(body)
    try:
        with smtplib.SMTP(os.environ["SMTP_HOST"], int(os.environ["SMTP_PORT"]), timeout=20) as server:
            server.ehlo()
            server.starttls(context=ssl.create_default_context())
            server.ehlo()
            server.login(os.environ["SMTP_USERNAME"], os.environ["SMTP_PASSWORD"])
            server.send_message(message)
        log.info("EMAIL_SENT subject=%s", subject, extra={"event": "email_sent", "stage": "alerts"})
        return True
    except Exception:
        log.exception("EMAIL_SEND_FAILED", extra={"event": "email_failed", "stage": "alerts"})
        return False
