#!/usr/bin/env bash
# Cleanup instructions - this script prints recommended commands and safety steps.
# WARNING: rewriting git history is destructive. Back up first.

set -e

echo "1) Create a full mirror backup of your repo (do this BEFORE rewriting history):"
echo "   git clone --mirror git@github.com:YOUR_OWNER/YOUR_REPO.git repo-backup.git"
echo 

echo "2) Remove sensitive files from HEAD and add to .gitignore:"
echo "   git rm --cached path/to/sensitive-file"
echo "   echo 'path/to/sensitive-file' >> .gitignore"
echo "   git commit -m 'Remove sensitive file from HEAD and add to .gitignore'"
echo 

echo "3) To scrub the file from all history (example using git-filter-repo):"
echo "   pip install git-filter-repo"
echo "   git clone --mirror https://github.com/YOUR_OWNER/YOUR_REPO.git repo-mirror.git"
echo "   cd repo-mirror.git"
echo "   # Remove a path from history:"
echo "   git filter-repo --path path/to/sensitive-file --invert-paths"
echo "   # OR remove files matching a regex:"
echo "   git filter-repo --replace-refs delete-no-add --path-glob 'secrets/**' --invert-paths"
echo "   # Force push the cleaned mirror back (be aware this rewrites history):"
echo "   git push --force --mirror origin"
echo 

echo "4) If you cannot rewrite history safely, rotate exposed keys and revoke them immediately."
echo 

echo "5) Add scanning + pre-commit hooks:"
echo "   pip install detect-secrets"
echo "   detect-secrets scan > .secrets.baseline"
echo "   # Install pre-commit hook to block commits containing secrets"
echo "   pip install pre-commit"
echo "   pre-commit install"
echo 

echo "6) After rotation, update the secrets in your backend secret manager(s) and update .env in your deploy environment (do NOT commit .env)."
echo 

echo "If you want, I can prepare a branch with the non-destructive changes (.gitignore, docs/SECURITY.md, proxy example, scan script)."