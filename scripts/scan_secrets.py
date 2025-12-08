#!/usr/bin/env python3
"""
Light-weight repo secret scanner (first-pass).
Searches files for common secret patterns:
 - Bitcoin WIF (starts with 5, K, or L)
 - Hex private keys (64 hex chars)
 - RSA private key blocks
 - AWS keys, Google API keys, Firebase keys, JWT secrets
This is a helpful starting point; for CI use gitleaks/detect-secrets/truffleHog.
"""
import re
import os
import sys

ROOT = os.getcwd()

patterns = {
    "WIF_private_key": re.compile(r"\b([KL5][1-9A-HJ-NP-Za-km-z]{50,51})\b"),
    "hex_privkey_64": re.compile(r"\b([a-fA-F0-9]{64})\b"),
    "rsa_private_block": re.compile(r"-----BEGIN (RSA )?PRIVATE KEY-----"),
    "aws_access_key": re.compile(r"\b(AKIA|ASIA)[A-Z0-9]{16}\b"),
    "google_api_key": re.compile(r"\bAIza[0-9A-Za-z-_]{35}\b"),
    "jwt_like": re.compile(r"[A-Za-z0-9-_]{20,}\.[A-Za-z0-9-_]{20,}\.[A-Za-z0-9-_]{20,}"),
    "firebase_api_key": re.compile(r"[A-Za-z0-9:_-]{20,}"),
}

ignore_dirs = {'.git', 'node_modules', 'dist', 'build'}

def scan_file(path):
    results = []
    try:
        with open(path, 'rb') as f:
            raw = f.read()
            try:
                text = raw.decode('utf-8', errors='ignore')
            except:
                return results
            for name, pat in patterns.items():
                for m in pat.finditer(text):
                    excerpt = text[max(0, m.start()-50):m.end()+50].replace('\n',' ')
                    results.append((name, m.group(0), excerpt))
    except Exception as e:
        # skip unreadable files
        return results
    return results

def walk_and_scan(root):
    findings = []
    for dirpath, dirnames, filenames in os.walk(root):
        # prune
        dirnames[:] = [d for d in dirnames if d not in ignore_dirs]
        for fn in filenames:
            path = os.path.join(dirpath, fn)
            # skip binary large files heuristically
            if os.path.getsize(path) > 2*1024*1024:
                continue
            res = scan_file(path)
            if res:
                findings.append((path, res))
    return findings

def main():
    print("Starting first-pass secret scan in", ROOT)
    findings = walk_and_scan(ROOT)
    if not findings:
        print("No probable secrets found in first-pass scan.")
        sys.exit(0)
    print("Potential secret matches (first-pass). Review manually.")
    for path, matches in findings:
        print("FILE:", path)
        for name, match, excerpt in matches:
            print("  PATTERN:", name)
            print("  MATCH:", match)
            print("  EXCERPT:", excerpt)
            print("  ---")
    print("If you find actual secrets, remove them from history and rotate them immediately.")

if __name__ == '__main__':
    main()
