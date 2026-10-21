#!/usr/bin/env bash
# Safe Preview: pushes a review branch in the user's existing repo, leaves main and prompted.fi alone.
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
for cmd in git gh python3; do command -v "$cmd" >/dev/null || { echo "Missing tool: $cmd"; exit 1; }; done
gh auth status >/dev/null || { echo 'GitHub CLI is not authenticated. Run: gh auth login'; exit 1; }
python3 "$ROOT/build.py"
REPO='jajja3890/prompted-site'
BRANCH="website-2026-10-21-rc2-$(date +%H%M%S)"
DEST="$(mktemp -d)"
trap 'rm -rf "$DEST"' EXIT
printf 'Cloning %s...\n' "$REPO"
gh repo clone "$REPO" "$DEST/site" -- --depth 1
cd "$DEST/site"
git switch -c "$BRANCH"
# Replace only on a new branch; preserve main and old production. No secret/env files.
for entry in * .[!.]* ..?*; do
  [ -e "$entry" ] || continue
  [ "$entry" = ".git" ] && continue
  rm -rf -- "$entry"
done
cp -R "$ROOT"/. .
rm -rf tools deploy-preview.sh .DS_Store 2>/dev/null || true
# Keep only the site release in the web repo.
git add -A
git commit -m 'feat(website): independent Prompted FI/EN site release candidate' 
git push -u origin "$BRANCH"
PR_URL="$(gh pr create --repo "$REPO" --base main --head "$BRANCH" --title 'Prompted FI/EN website — independent release candidate' --body 'Standalone, zero-Lovable-runtime marketing site. Production domain unchanged. PRELAUNCH_NOINDEX remains active. Needs visual, content, privacy and DNS cutover approval before merge.')"
printf '\nPREVIEW BRANCH CREATED (old live site unchanged)\n%s\n' "$PR_URL"
printf 'Open the PR and check whether a Vercel preview deployment was created. Do not merge until reviewed.\n'
