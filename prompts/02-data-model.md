# Prompt 02 Model decisions and evidence

```text
Read the project instructions and current tests. Design the smallest SQLite schema that supports company, person, employment, opportunity, interaction, action, rubric version, assessment, and evidence records.

Requirements:
- direct tables and foreign keys, no generic graph abstraction;
- unknown is represented explicitly and differs from zero or false;
- every evidence item has source type, source reference, observed date, captured date, and optional expiry date;
- every assessment records the rubric version and evidence IDs it used;
- fit, evidence confidence, hard-constraint result, and current priority are separate fields;
- private text stays in $COMPASS_DATA_DIR;
- migrations are deterministic and reversible during development.

Write schema tests before implementation. Include tests for former employment, conflicting evidence, stale evidence, several roles at one company, and a rubric change that preserves old assessments.

Use synthetic names only. Run the tests, print only record IDs and counts, show the schema in plain language, and stop for review.
```
