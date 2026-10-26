# Cloudflare setup
1. Install Node.js and Wrangler, then run `npm install -g wrangler` and `wrangler login`.
2. Create D1: `wrangler d1 create mihigo-jobs`; create R2: `wrangler r2 bucket create mihigo-media`.
3. Copy `wrangler.toml.example` to `wrangler.toml`; fill the returned D1 ID and confirm bucket binding.
4. Apply schema: `wrangler d1 execute mihigo-jobs --file=./schema.sql`.
5. Add `INTERNAL_API_TOKEN` with `wrangler secret put INTERNAL_API_TOKEN`; use secrets for other credentials.
6. Deploy with `wrangler deploy`. Test `/health`, then authenticated `POST /api/jobs`.
7. The Worker only queues and scans jobs. Connect a real Kaggle dispatch adapter and result-reporting endpoint before expecting processing.
8. Configure Cron Trigger and verify logs. Cron does not provide GPU compute.
