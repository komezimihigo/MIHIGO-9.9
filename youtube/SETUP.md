# YouTube publishing setup
1. Create/select a Google Cloud project and enable YouTube Data API v3.
2. Configure OAuth consent and redirect URI; create the appropriate OAuth client.
3. Authorize each target channel separately as required and store refresh tokens in a secret manager.
4. Implement the official API client with resumable upload and persist the returned video ID.
5. Start with `privacyStatus=private`. Validate each format and metadata.
6. If an upload times out after starting, reconcile status before retrying to prevent duplicates.
7. Check current quota, API verification and upload restrictions. API upload success does not guarantee monetization eligibility.
