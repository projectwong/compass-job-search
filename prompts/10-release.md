# Prompt 10 Prepare the public repository

```text
Prepare this project for a public GitHub repository without publishing any real job-search data.

Work from a clean directory and inspect the full Git history. Audit for:
- names, email addresses, phone numbers, and profile URLs;
- resume phrases, employer-specific notes, compensation, and application history;
- contact exports, messages, meeting notes, databases, documents, images, logs, and snapshots;
- credentials, tokens, environment files, and local paths;
- deleted files that remain in Git history.

Keep only code, schemas, prompts, documentation, and synthetic fixtures. Replace examples rather than redacting them in place when there is any doubt. Confirm that fictional fixtures cannot be mistaken for real people or companies.

Then verify a fresh clone can:
1. read the setup instructions;
2. create a private data directory outside the repository;
3. run the synthetic tests and demo;
4. fail safely without private configuration.

Produce a release report listing every check, its result, and any unresolved risk. Do not create or publish the GitHub repository until I approve that report.
```
