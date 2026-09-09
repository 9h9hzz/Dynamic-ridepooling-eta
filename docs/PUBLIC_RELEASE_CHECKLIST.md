# Public release checklist

Complete every item before switching the GitHub repository to Public.

## Review and authorship

- [ ] Confirm whether the current venue uses double-blind review.
- [ ] Confirm that a public repository is permitted during review.
- [ ] Obtain any required approval from the supervisor and co-authors.
- [ ] Confirm ownership of the simulation and model code selected for release.
- [ ] Check licenses for any adapted or third-party implementation.

## Identity and anonymity

- [ ] Remove names, student IDs, email addresses, institutions, supervisors, and acknowledgements.
- [ ] Avoid the exact manuscript title if it can identify the submission.
- [ ] Remove absolute local paths and usernames from code, notebooks, metadata, and images.
- [ ] Remove document properties and image metadata that may identify the author.
- [ ] Check Git commit author name and email before the first public push.

## Data and results

- [ ] Do not include raw or licensed data.
- [ ] Do not include the full generated passenger-level dataset.
- [ ] Do not include complete simulation matrices or route lookup files.
- [ ] Do not include model checkpoints, prediction dumps, or full experiment outputs.
- [ ] Publish only figures and numbers specifically cleared for portfolio use.
- [ ] Prefer synthetic samples for runnable demonstrations.

## Final repository scan

Run these checks from the repository root:

```bash
git status --short
git ls-files
git grep -n -i -E "student|university|supervisor|author|email|submission|manuscript"
```

Then inspect the GitHub file list in a private repository before changing visibility.

