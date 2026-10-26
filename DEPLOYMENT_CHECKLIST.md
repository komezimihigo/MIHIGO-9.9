# Acceptance checklist
- [ ] Secrets absent from ZIP and repository.
- [ ] Cloudflare D1/R2 deployed; authenticated intake tested.
- [ ] Ratio policy tested across rolling outputs (50% vertical, 50% landscape).
- [ ] Rights gate rejects missing/unclear evidence.
- [ ] Source discovery uses permitted APIs/download methods and records license evidence.
- [ ] Kaggle atomic claim/report endpoint and R2 upload/download adapters implemented.
- [ ] Actual FFmpeg rendering creates both aspect ratios; ffprobe validates duration/audio/codec.
- [ ] AI model and fallback configured with rate/cost limits.
- [ ] YouTube OAuth works for every channel; private test uploads pass.
- [ ] SMTP email test received; worker crash and quota exhaustion alerts tested.
- [ ] Watchdog recovers abandoned job; duplicate event does not duplicate upload.
- [ ] 72-hour unattended test passed.
- [ ] Free quotas and actual daily throughput measured.
- [ ] Public publishing enabled only after all above pass.
Do not claim production readiness while any adapter is a placeholder or raises NotImplementedError.
