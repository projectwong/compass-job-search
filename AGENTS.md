# Compass harness instructions

## Mission

Build the smallest local-first job-search system that makes the user's next action clear without inventing facts. This repository is the specification and starter kit. Build the user's implementation in a separate working directory or repository.

## Read before changing anything

1. Read `README.md`, `docs/privacy.md`, and `docs/build-log.md`.
2. Read the current numbered prompt in `prompts/`.
3. State the assumptions, open decisions, and acceptance check for the phase.
4. Confirm that `COMPASS_DATA_DIR` points outside every public repository before accepting real data.

Work through the phases in numerical order. Stop after each phase, show the changed files and check results, then ask the user whether to continue.

## Privacy boundary

- Only code, schemas, prompts, documentation, and synthetic fixtures belong in a public repository.
- Real resumes, contacts, messages, notes, research, opportunity records, databases, tokens, and credentials belong in `COMPASS_DATA_DIR`.
- Never copy private data into fixtures, logs, screenshots, test snapshots, or commit messages.
- Never print full private records during tests. Use counts, record IDs, and redacted errors.
- If a requested action would cross this boundary, stop and name the data and destination involved.

## Product invariants

- Unknown stays unknown.
- Evidence and its source travel together.
- Eligibility, fit, confidence, and priority remain separate.
- A warm path means a person the user actually knows who is currently at the company.
- Every active opportunity has one next action and one date.
- A company enters the working set only when there is a real action to take.
- Job-board connectors monitor only companies in the hand-curated target universe.
- First-party job-board ingestion is core, not an optional extension.
- No message is sent and no application is submitted automatically.

## Build rules

- Begin with Markdown, YAML, SQLite, and standard-library Python unless the user chooses another stack.
- Keep the workflow usable without a dashboard for two weekly reviews.
- Write a failing test before fixing a bug or adding scoring behavior.
- Do not add an agent framework, vector database, hosted dependency, or authenticated scraper without a demonstrated need and explicit approval.
- Run the phase acceptance checks before finishing.
