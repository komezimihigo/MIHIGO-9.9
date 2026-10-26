# Kaggle batch worker
Kaggle is temporary batch compute, not an always-on service. Schedule runs only after claim/report endpoints and R2 adapters are implemented.
Add these as Kaggle Secrets: `MIHIGO_API_URL`, `MIHIGO_INTERNAL_API_TOKEN`, `R2_ENDPOINT_URL`, `R2_ACCESS_KEY_ID`, `R2_SECRET_ACCESS_KEY`, `R2_BUCKET`, optional AI-provider keys. Never hardcode secrets.
Outputs must be uploaded to persistent R2 before the session ends. Scheduled notebook availability and quotas are not guaranteed.
