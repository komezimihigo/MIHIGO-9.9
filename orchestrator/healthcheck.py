import logging, os, platform, sys
from .logging_setup import configure
from .alerts import send_email

def main():
    log = configure()
    log.info("HEALTHCHECK_STARTED platform=%s python=%s", platform.platform(), sys.version)
    required = ("INTERNAL_API_TOKEN",)
    missing = [k for k in required if not os.getenv(k)]
    if missing:
        log.error("CONFIG_ERROR missing=%s", missing, extra={"event":"config_error","stage":"healthcheck"})
        send_email("Configuration error", "MIHIGO 9.8 missing required configuration: " + ", ".join(missing))
        return 2
    log.info("HEALTHCHECK_OK", extra={"event":"healthcheck_ok","stage":"healthcheck"})
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
