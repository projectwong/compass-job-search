# Prompt 07A Build a sourced proof-point library

```text
Build a private proof-point library for application, resume, and interview preparation. Do not generate a new resume format until the library validates.

Each proof point needs a stable ID, employer or context, date range, claim, scope, outcome, source reference, confidence, allowed wording, prohibited upgrade, and tags for role families or capabilities. Unknown numbers remain unknown. Conflicting sources remain visible.

Add a deterministic selector that receives a normalized role record and returns the smallest relevant set of proof-point IDs with reasons. Selection may use explicit tags and rules, not an opaque model score. Add a drift check that fails when generated text includes a number, title, employer, date, or result not supported by the selected proof points.

Claude may propose a fit summary, gaps, resume variant, interview story set, or outreach draft. Every statement must cite an input evidence or proof-point ID, or be labeled as an inference. Store outputs as proposals and require explicit confirmation before changing any canonical record. Never send or apply automatically.

Generated resume variants and interview briefs are disposable views in $COMPASS_DATA_DIR. They must identify the proof-point IDs used and must never become a new source of truth. The rest of Compass must work without an AI API key.

Write tests for unsupported numbers, title inflation, conflicting dates, omitted limitations, fabricated facts, deterministic selection, rejected proposals, and regeneration from the same inputs. Use a fictional career history in tests. Show the validation report and stop.
```
