# Security, copyright and free-tier limits
- Never commit `.env`, OAuth token files, API tokens, Kaggle credentials or service-account JSON.
- Use least-privilege credentials and platform secret managers. Redact tokens, passwords and signed URLs from logs/emails.
- A disclaimer does not grant copyright permission. Prefer owned content, public-domain content with verified status, or licenses explicitly allowing commercial reuse and modifications.
- Record source URL, creator, license name/URL, evidence, retrieval date and attribution requirements. Reject unknown rights by default. Automated screening is not legal certainty.
- Do not bypass DRM, access controls, login restrictions or source platform terms. Use permitted APIs/download methods.
- Licensed content can still fail YouTube reused-content monetization rules; meaningful original commentary/analysis may be needed.
- Cloudflare Workers are for orchestration, not FFmpeg/GPU rendering. R2 stores files, not processing. Kaggle sessions are finite and quota-limited. Cloud Run free allowances do not provide free GPUs. GitHub Actions schedules are not guaranteed real-time triggers.
- If all compute is unavailable, preserve jobs and resume later; never claim work completed when it did not.
