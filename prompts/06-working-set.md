# Prompt 06 Build the working set and daily actions

```text
Build the Markdown working set and daily action view. Do not build a web interface.

Promote a target into the working set only when it has a live opportunity, a person worth contacting, or a research question that can change a decision. Use templates/company.md and templates/person.md as starting points, changing them only when the data model requires it.

Each action needs a stable ID, status, due date, created date, updated date, and an optional link to a company, person, or opportunity. One action has one canonical record. Daily and weekly views are derived, never duplicated sources of truth.

Add commands to:
- promote a company;
- add or close an action;
- list today's actions;
- list overdue follow-ups;
- list blocked actions;
- validate broken links and duplicate IDs.

Write tests first. Use synthetic private data. Run the commands against the fixtures, show the derived output, and stop.
```
