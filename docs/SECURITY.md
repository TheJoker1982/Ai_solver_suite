# Security and Secrets Handling Guide

This file documents incident response, secrets management, and step-by-step cleanup recommendations for the Crypto Heist repo.

Important: If any private key, API secret, or credential has been committed, treat the secret as compromised and rotate it immediately. Do NOT attempt to reuse exposed private keys for any purpose.

1) Immediate triage (first 0–30 minutes)
- Identify the exposed items: run a secret scan (see /scripts/scan_secrets.py).
- Take the repo offline for pushes or inform collaborators to avoid pushing further secrets.
- Remove the file(s) from the working tree (git rm --cached <file>) and add them to .gitignore.
- Revoke and rotate any exposed credentials immediately (API keys, service accounts, private keys). Treat private keys as compromised.

2) Remove secrets from git history (careful — this rewrites history)
- Recommended tools: git-filter-repo (preferred), BFG (alternative).
- Example (git-filter-repo):
  - Install: pip install git-filter-repo (or use system package)
  - Make a backup clone: git clone --mirror https://github.com/<owner>/<repo>.git repo-backup.git
  - Rewrite: git filter-repo --path path/to/exposed-file --invert-paths
  - Force-push rewritten history to the repository: git push --force
- If you prefer BFG:
  - Install BFG jar
  - java -jar bfg.jar --delete-files IDENTITY_FILE repo.git
  - Follow BFG docs; always have a backup.

3) Rotate compromised keys
- For each rotated secret, update your backend secret store:
  - AWS: Secrets Manager or Systems Manager Parameter Store
  - GCP: Secret Manager
  - Azure: Key Vault
  - Heroku / Vercel / Netlify: use platform environment variables
- Regenerate fresh keys, update services, and verify operations.

4) Prevent future leaks
- Add scanning tools on CI:
  - gitleaks, detection-secrets, truffleHog or GitHub secret scanning
  - Fail PRs that contain secrets
- Add pre-commit hook to block accidental commits: pre-commit with detect-secrets
- Move all credentials to secure secrets store (do not use .env in VCS)

5) Organize & label secrets
- Use consistent naming and metadata (example naming below):
  - BLOCKSTREAM_API_URL (public endpoint)
  - BLOCKSTREAM_API_KEY (if you use an API key)
  - BLOCKCHAIR_API_KEY
  - ETH_RPC_URL (alchemy/infura/llamarpc)
  - FIREBASE_URL
  - FIREBASE_API_KEY
  - TRUST_WALLET_PREDICTION_KEY
  - SSH_DEPLOY_KEY_NAME
- In your backend secret store add metadata tags: owner, environment (dev/staging/prod), purpose, rotation_date, contact.

6) Logging & auditing
- Log secret accesses (IAM audit logs)
- Short TTLs where possible. Rotate periodically.

7) Incident reporting checklist
- Date/time discovered
- Secret(s) discovered
- Actions taken (files removed, keys rotated)
- List of services notified
- Postmortem summary

Appendix: Helpful commands
- Show files containing a string (local):
  - git grep -n "PRIVATE_KEY"
- Remove from current history (working tree only):
  - git rm --cached path/to/file
  - echo "path/to/file" >> .gitignore
  - git commit -m "Remove sensitive file and add to .gitignore"
- Rewriting history: see section (use git-filter-repo or BFG