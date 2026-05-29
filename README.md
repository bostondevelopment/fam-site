# Fam — a private family graph

A two-platform consumer app for keeping a family's people, photos, and memories in one place. Private to the family; no ads, no tracking, no public posts.

→ **[The app + what it does](https://bostondevelopment.github.io/fam-site/)**
→ **[Engineering deep-dive](https://bostondevelopment.github.io/fam-site/engineering.html)** — backend, agent workflow, signed-media CDN, OpenAPI contract
→ **[Design packet](https://bostondevelopment.github.io/fam-site/design.html)** — principles, tokens, components, motion

---

## About this repo

This repository hosts the public-facing site for Fam — landing page, engineering write-up, design packet, privacy policy. The Fam app itself (Django 5.2 / DRF backend + Expo / React Native mobile) lives in a separate, private repository.

## About the app

Fam is a private family-graph product. The people you love, the photos you've taken of them, the birthdays and anniversaries and holidays that mark a year together — all in one place, visible only to your family. A Pulse feed surfaces what's coming up next; AI-suggested face tagging fills in old photo albums; an elder-to-caregiver transfer flow lets accounts be handed off without losing history.

**Status:** TestFlight beta (not the App Store, by choice).

## How it was built — honest framing

Fam was built solo by **directing AI coding agents (Claude Code, Cursor)** through a codified 9-role agent workflow checked into the repo — not by hand-writing the code. The repeatable, transferable artifact is the workflow itself: prompts for product → architect → designer → brief → developer → QA → design-audit → release, slash-command bindings in the IDE, and an `AGENTS.md` router with a cost guardrail that forces the agent to stop before any paid-service usage.

The output is a real two-platform product with the engineering discipline of a small team:

- **132 documented API endpoints** (OpenAPI contract drives the auto-generated mobile client; a CI step fails the build when the contract and client drift).
- **54 Django models** across **15 service domains** (`activity`, `events`, `faces`, `notes`, `notifications`, `occurrences`, `people`, `photos`, `pulse`, `reminders`, `transfer_requests`, …).
- **271 archived pull requests** with an enforced naming convention — every commit title matches its PR archive filename, turning the git log into a readable product changelog.
- **42 Maestro E2E flows** on a real iOS simulator gating CI, plus **40 bash smoke suites** running against the live server end-to-end.
- An **AWS Rekognition face-tagging pipeline**, **CloudFront signed-media URLs** (dual mode: per-URL query signing + cookie-based wildcard, with S3 presigned fallback), **IDOR security hardening** with a dedicated test suite, and an **occurrence-materialization feed** reconciled by Celery.
- Full GitHub Actions CI/CD, EAS build profiles, and a local iOS code-signing pipeline → TestFlight.

The **[engineering page](https://bostondevelopment.github.io/fam-site/engineering.html)** walks through all of it.

---

## Author

Built by **Michael Finneran** — Boston, MA
[linkedin.com/in/michaelfinneran](https://linkedin.com/in/michaelfinneran) · [MRFinneran@gmail.com](mailto:MRFinneran@gmail.com)
