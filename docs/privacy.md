# Privacy Model

Compass contains information about you and other people. Treat privacy as an architectural boundary, not a note in the README.

## Public repository

The public repository may contain code, schemas, prompts, documentation, and unmistakably synthetic fixtures. It must not contain real resumes, contact exports, messages, meeting notes, opportunity records, research, databases, raw job-board responses, logs, screenshots, generated documents, or credentials.

## Private data directory

All real data lives in `COMPASS_DATA_DIR`, outside the repository. Restrict access using the operating system, include it in an encrypted backup you control, and test restore before trusting the backup.

Do not copy private data into the repository to debug a test. Create the smallest synthetic record that reproduces the behavior.

## AI access

Decide which private files Claude may read before starting a session. Frontmatter labels such as `private` do not enforce access. Directory boundaries and tool permissions do.

Start sensitive work in plan mode, review requested file access, and approve only the directories needed for the current phase. Avoid putting raw messages or full contact exports into prompts when a structured subset will answer the question.

## Other people's data

A contact export describes other people, not only you. Use it for the purpose it was obtained for, keep it local by default, and promote only the small working set you genuinely need. Do not infer sensitive traits, relationship strength, or willingness to help.

## Job-board data

Use public, first-party feeds and respect their access rules. Enforce request pacing, identify the client when a provider expects it, retain raw responses privately, and keep provider failures visible. Never treat a missing role from a failed or partial scan as a closed posting.

## Public release

Create a new repository with new Git history. Do not make a private lifetime repository public after deleting private files, because deleted files remain in earlier commits. Audit current files and the full history before release.

The included checker catches dangerous file types and common credential formats. It cannot recognize every personal detail, so a human content review remains required.
