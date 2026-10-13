# Compass project instructions

## Goal

Build the smallest local-first job-search system that makes the user's next action clear without inventing facts.

## Before coding

- Read `README.md`, `docs/build-log.md`, and the current numbered prompt.
- State assumptions and ambiguities before changing files.
- Define the acceptance check for the current phase.
- Prefer a manual Markdown workflow until repeated use proves code is needed.

## Privacy boundary

- This repository is public-safe. Only code, schemas, prompts, documentation, and synthetic fixtures belong here.
- Real resumes, contact exports, messages, meeting notes, company research, opportunity records, databases, tokens, and credentials live in `COMPASS_DATA_DIR`, which must be outside this repository.
- Never copy private data into fixtures, logs, screenshots, test snapshots, or commit messages.
- Never print full private records during tests. Use counts, record IDs, and redacted errors.
- If a task would cross this boundary, stop and explain the exact file and data involved.

## Product invariants

- Unknown stays unknown.
- Evidence and its source travel together.
- Hard constraints, fit, confidence, and priority remain separate.
- A warm path means a person the user actually knows and who is currently at the company.
- No message is sent and no application is submitted automatically.
- Every active opportunity has one next action and one date.
- A company enters the working set only when there is a real action to take.
- Job-board connectors monitor only companies in the hand-curated target universe.
- Connector output records published facts; scoring and owner disposition happen later.

## Coding rules

- Use standard-library Python and SQLite unless the user approves another dependency.
- Write a failing test before fixing a bug or adding scoring behavior.
- Keep modules small and direct. Do not add a service, agent framework, vector database, or hosted dependency without evidence that the current workflow needs it.
- Run the phase acceptance checks before finishing.
- Show changed files and test results, then stop.
