# Prompt 03A Add first-party job-board ingestion

```text
Build the first-party job-board ingestion layer for companies already present in my hand-curated target universe. Do not discover or add target companies automatically.

Define a small provider-adapter interface. Each connector fetches a public, first-party applicant-tracking-system feed and returns normalized roles with:
- provider and external ID;
- target company ID;
- title, location, department, description, work-model evidence, and canonical URL;
- first seen, last seen, provider updated, and closed dates;
- content hash and raw private source reference;
- open or closed posting state.

Implement one provider first, selected from the providers used by my current target list. Use recorded synthetic fixtures in tests. Do not scrape authenticated pages, bypass access controls, or add a general crawler.

Keep discovery separate from scoring and owner judgment. Posting state must remain separate from pursue, snooze, dismiss, applied, and closed application dispositions.

Enforce request pacing, timeouts, bounded retries, provider-specific identification where appropriate, and isolated failure handling. Store raw responses only in $COMPASS_DATA_DIR. One broken provider must not stop the rest of a scan.

Write adapter contract tests plus tests for pagination, duplicate roles, changed content, disappeared roles, malformed responses, request limits, repeated scans, and partial provider failure. A role missing from a successful complete scan closes without deletion; a failed or partial scan must not close roles.

Demonstrate with synthetic fixtures. Show the normalized records, revision diff, scanner-health output, and test results, then stop before adding another provider.
```
