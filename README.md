# MIHIGO 9.8 — Autonomous Video Factory
This is a zero-cost-first deployment scaffold for an autonomous multi-channel video pipeline. It includes platform-specific folders, setup guides, job-state/policy code, logs, email alerts, Cloudflare Worker/D1 control-plane starter, Kaggle batch-worker starter, Cloud Run fallback starter, source-rights gate, YouTube publishing contract, and offline tests.

## Required video mix
Target 50% vertical Shorts (9:16, 30–60s) and 50% standard landscape uploads (16:9, 30–60s or longer if configured). “Standard” means landscape upload format, not a guarantee of YouTube's classification. The scheduler should balance the rolling output mix across enabled channels.

## Reality check
This ZIP is a structured starter project, not a claim that all provider integrations are live. Kaggle sessions are temporary; Cloudflare Workers cannot render videos; Cloud Run's free allowance is not free GPU compute; free-tier limits vary. The system can queue/retry without human action, but 20+ finished videos every day at $0 cannot be guaranteed. Provider adapters marked TODO must be implemented and tested before production.

## Structure
- `cloudflare/`: Worker API, Cron scan, D1 schema and deployment instructions.
- `kaggle/`: scheduled batch worker and Kaggle setup.
- `workers/cloud_run/`: independent CPU/serverless fallback scaffold.
- `orchestrator/`: job state, output ratio policy, rights gate, retries, logs and SMTP alerts.
- `discovery/`: source candidate contract and manifest example.
- `youtube/`: publishing/OAuth setup and safe publisher contract.
- `tests/`: offline policy tests.
- `.env.example`: placeholders only; never commit real secrets.

## First deployment
1. Read `SECURITY_AND_LIMITS.md`.
2. Set up Cloudflare D1/R2 following `cloudflare/SETUP.md`.
3. Add secrets through platform secret managers, not source code.
4. Configure Kaggle Secrets and schedule the notebook only after its claim/report API is connected.
5. Configure YouTube OAuth per channel and start with private uploads.
6. Run `python -m unittest discover -s tests -v`.
7. Follow `DEPLOYMENT_CHECKLIST.md`; don't enable public autonomous publishing until all provider adapters pass end-to-end tests.

Every service logs startup, job IDs, stages, retries and tracebacks. Secrets are never intentionally printed.
