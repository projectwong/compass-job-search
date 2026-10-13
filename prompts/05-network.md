# Prompt 05 Map warm paths

```text
Build a local import and matching workflow for a contact export stored in $COMPASS_DATA_DIR. Do not scrape a website or call a hosted enrichment service.

Normalize names, profile URLs, employer text, title, connection date, and import date while preserving the raw source outside the database. Model employment history so current and former employers are distinct.

A warm path qualifies only when:
- I know the person directly;
- current employment at the target company is verified;
- I would contact the person without needing an introduction.

Everything else is a lead or an uncertain match. Company alias matching must be reviewable. Never silently accept a fuzzy match.

Write tests for former employees, duplicate contacts, employer aliases, missing current-employment dates, uncertain matches, and re-imports. Add a command that shows each target's qualified warm paths, uncertain candidates, and the evidence behind both.

Use synthetic contacts in every test and demonstration. Show counts and fictional names only, then stop.
```
