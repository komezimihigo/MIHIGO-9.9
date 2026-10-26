# Cloud Run fallback candidate
Use only after verifying current free-tier terms and setting billing budgets/alerts if billing is enabled. This is a CPU/serverless fallback, not free GPU compute. Run one bounded job per invocation; fetch source from R2, validate rights, render, upload output, update D1, and exit. Never rely on a permanently running process.
