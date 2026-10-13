# Compass Job Search Build Log

This log takes you from an empty repository to a working personal job-search system. Each entry has a purpose, a Claude prompt, a human decision, and an acceptance check. Run the entries in order and commit after each accepted phase.

## Entry 0 Define the search before the system

The first failure mode is building a company-ranking machine before deciding what a good job means. Start with an interview that produces a rubric you can disagree with.

Create a private sibling directory and point an environment variable at it:

```bash
mkdir ../compass-private
export COMPASS_DATA_DIR="$(cd ../compass-private && pwd)"
claude --permission-mode plan
```

Run [`prompts/00-rubric.md`](../prompts/00-rubric.md). Answer with real tradeoffs, not adjectives. "Interesting work" is not a criterion until you can describe evidence for and against it.

Accept this phase when the rubric contains:

- hard constraints with explicit pass, fail, and unknown behavior;
- company preferences and role preferences kept separate;
- examples of attractive and unattractive tradeoffs;
- a short statement of what the search is optimizing;
- a list of facts the system must never infer.

Commit only the schema and synthetic example. The real rubric stays outside Git.

## Entry 1 Establish the public and private boundary

Run [`prompts/01-boundary.md`](../prompts/01-boundary.md). Claude should create a configuration loader that refuses to run when `COMPASS_DATA_DIR` is missing, points inside the repository, or has unsafe permissions where the operating system exposes them.

The key decision is that private data does not merely appear in `.gitignore`. It lives outside the repository. Ignore rules reduce accidents, but they do not erase Git history.

Accept this phase when:

- the app refuses an in-repository private path;
- logs and errors do not echo resume or contact contents;
- synthetic fixtures run without access to private data;
- a secret scan and repository file audit pass.

## Entry 2 Model decisions and evidence

Run [`prompts/02-data-model.md`](../prompts/02-data-model.md). The model should support company, person, opportunity, interaction, action, rubric, assessment, and evidence records.

Do not begin with a generic knowledge graph. Use direct tables and foreign keys. Every assessment must record the rubric version and supporting evidence, because a score without its inputs becomes folklore.

Accept this phase when tests prove:

- unknown differs from zero;
- stale evidence remains visible;
- one person can have employment history without being treated as a current warm path;
- one company can have several opportunities without duplicating company research;
- changing the rubric does not silently rewrite earlier assessments.

## Entry 3 Build the target universe by hand

Run [`prompts/03-targets.md`](../prompts/03-targets.md). Start with companies you can name and defend. Importing a large discovery feed feels productive, but it postpones the judgment the system needs.

The universe can live in a private CSV or YAML file at first. Require a source, a date, and a one-sentence reason for inclusion. Separate the universe from the working set: a company gets a full note only when there is an action to take.

Accept this phase when you can add, update, archive, and list targets without creating duplicate companies, and when every listed fact is sourced or marked unknown.

## Entry 4 Monitor first-party job boards

Run [`prompts/03a-job-discovery.md`](../prompts/03a-job-discovery.md). This is not a general web crawler. Each supported applicant-tracking system gets a small adapter that converts its public response into one normalized role record.

Keep discovery separate from judgment. The connector records what a company published; the rubric decides whether it deserves attention. Store the raw response privately so parser errors can be diagnosed, but expose only normalized fields to the rest of the system.

Start with the provider used by the largest share of your target list, then add providers one at a time. A connector must enforce request pacing, bounded retries, and timeouts. One failing provider cannot stop the others.

Accept this phase when:

- repeated scans are idempotent;
- one broken provider does not fail the run;
- changed postings retain a visible field-level revision;
- roles missing from a successful complete scan close without being deleted;
- posting state remains separate from your pursue, snooze, dismiss, or applied decision;
- request limits are enforced in code rather than merely documented.

## Entry 5 Score fit without manufacturing certainty

Run [`prompts/04-scoring.md`](../prompts/04-scoring.md). Use hard constraints first, then fit, then evidence confidence. Keep current priority outside the fit score.

A useful result looks like this:

```text
Company: Northstar Systems
Eligibility: unknown, work model is unverified
Fit: promising, 3 of 5 weighted criteria have evidence
Confidence: low
Priority: research next, no active opportunity
```

It does not look like `87.4% match` unless the inputs justify that precision.

Accept this phase when tests cover failed constraints, unknown constraints, missing evidence, conflicting evidence, rubric version changes, and stable tie behavior.

## Entry 6 Map real warm paths

Run [`prompts/05-network.md`](../prompts/05-network.md). Import only a local contact export that you are entitled to use. Preserve the raw file outside Git and normalize into the private database.

The warm-path rule is intentionally strict: you know the person, their current employer is verified, and you would contact them directly. A second-degree connection, an old employer, or a scraped name is a lead, not a warm path.

Accept this phase when:

- employer aliases can be reviewed rather than silently merged;
- former employees never count as current warm paths;
- uncertain matches appear in a review queue;
- the output shows why each path qualifies;
- deleting the raw import does not break the normalized private store.

## Entry 7 Create the working set and action loop

Run [`prompts/06-working-set.md`](../prompts/06-working-set.md). Promote a company from the universe only when one of these exists:

- a live role worth evaluating;
- a person worth contacting;
- a research question that will change a decision.

Use the company page as the context surface and a daily list as the execution surface. Each open action gets a stable ID, status, due date, and link back to its company, person, or opportunity.

Accept this phase when a single command can show today's actions, overdue follow-ups, and blocked items without duplicating tasks across files.

## Entry 8 Track opportunities and conversations

Run [`prompts/07-pipeline.md`](../prompts/07-pipeline.md). Model an opportunity as a role at a company, not as the company itself. Keep the job description, application state, contacts, interview stages, decision, and next action together.

Use conversation briefs for important calls. A brief should say why the conversation matters, what you need to learn, which two or three accomplishments are relevant, and the specific next step you want. Afterward, record commitments on both sides and date the follow-up.

Accept this phase when every active opportunity has exactly one next action, closed opportunities retain history, and no application or message can be sent by the system.

## Entry 9 Build a sourced proof-point library

Run [`prompts/07a-proof-points.md`](../prompts/07a-proof-points.md) when the first real opportunity reaches application or interview preparation. A proof point is a sourced career claim with a stable ID, scope, result, date range, allowed wording, and known limitation.

Claude may select relevant proof points for a role, but it may not upgrade a claim, fill in a missing number, or resolve conflicting sources. Generated resumes and briefs are disposable views over the private library, never the source of truth.

Accept this phase when every generated claim traces to a proof-point ID, unsupported numbers fail validation, contradictory claims are surfaced, and output regenerates deterministically from the same inputs.

## Entry 10 Add the weekly learning loop

Run [`prompts/08-review.md`](../prompts/08-review.md). The weekly review is where the system earns its right to grow. Review target changes, pipeline movement, overdue follow-ups, useful conversations, changed assumptions, and repeated manual friction.

Do not add automation after one annoying afternoon. Record the friction and wait for it to recur in two weekly reviews. That delay distinguishes a workflow problem from a bad day.

Accept this phase when the review can explain why priorities changed and can name the evidence that caused each change.

## Entry 11 Build the smallest interface

Run [`prompts/09-interface.md`](../prompts/09-interface.md) only after the file workflow has survived two weekly reviews. The default interface is a local read-only dashboard backed by an exported snapshot, not direct database writes.

Lead with gaps and next actions:

- target companies with no warm path;
- overdue follow-ups;
- active opportunities with no next action;
- evidence that is stale or missing.

Accept this phase when the interface makes no network requests, binds only to localhost, exposes no private values in client logs, and can be deleted without losing source data.

## Entry 12 Prepare a public release

Run [`prompts/10-release.md`](../prompts/10-release.md). Release only code, schemas, prompts, documentation, and synthetic examples. Create a new repository from a clean directory rather than changing a private repository to public.

Before publishing, inspect the full Git history, not only the current tree. Search for names, email addresses, phone numbers, employer-specific notes, credentials, resume phrases, contact exports, database files, screenshots, and generated test snapshots.

Accept this phase only when another person can clone the repository, run the synthetic demo, and understand where private data must live without receiving any of yours.

## What to build next

After the first month, build only from observed friction. Reasonable candidates include employer-change review, meeting-note filing, response reminders, and interview prep. Each one changes the privacy or correctness surface, so treat it as a new decision with its own acceptance test.

The system is working when it reduces dropped follow-ups and weak decisions. More records, more automation, and more dashboards are not success measures.
