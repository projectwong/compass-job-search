# Prompt 03 Build the target universe

```text
Implement the smallest import and review workflow for a hand-built target-company universe.

Each target needs a canonical name, optional domain, reason for inclusion, source, observed date, status, and aliases. Preserve the original input. Make imports idempotent. Never merge companies automatically when the match is uncertain, create a review item instead.

Keep the full universe separate from the working set. A company should not receive a detailed note until there is a live role, a person to contact, or a research question that can change a decision.

Start with YAML or CSV in $COMPASS_DATA_DIR. Do not add scraping, external discovery, or an admin UI. Write tests for duplicate names, aliases, malformed dates, repeated imports, archiving, and unknown facts.

Add a command that lists the universe with one sentence explaining why each company is present. Run tests and demonstrate it only with synthetic fixtures.
```
