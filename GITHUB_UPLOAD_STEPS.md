# Upload to GitHub

Keep the repository private until the public-release checklist is complete.

## Option A: GitHub website

1. On GitHub, select **New repository**.
2. Use the name `dynamic-ridepooling-eta`.
3. Paste the Description from `REPOSITORY_METADATA.md`.
4. Select **Private**.
5. Do not add a README, `.gitignore`, or license on GitHub; they already exist locally.
6. Create the empty repository.
7. Follow GitHub's “push an existing repository from the command line” instructions from this folder.
8. Add the Topics listed in `REPOSITORY_METADATA.md`.
9. Review the complete file list on GitHub before considering a visibility change.

## Option B: GitHub CLI

After installing and signing in to GitHub CLI, run from this folder:

```bash
git init
git add .
git status
git commit -m "Create publication-safe portfolio repository"
gh repo create dynamic-ridepooling-eta --private --source=. --remote=origin --push
```

Do not replace `--private` with `--public` until the venue policy, approvals, file provenance, and release checklist are all confirmed.

