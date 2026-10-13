# Prompt 00 Define the rubric

```text
You are helping me define the decision model for a personal job search. Do not write code yet.

Interview me one question at a time. Your goal is to produce a private rubric that distinguishes:
1. hard constraints;
2. company-level preferences;
3. role-level preferences;
4. working-arrangement preferences;
5. current search priorities that may change quickly.

For every criterion, ask what observable evidence would support it, contradict it, or leave it unknown. Force tradeoffs with paired examples. Do not accept adjectives such as "interesting," "good culture," or "high impact" until I define what I would observe. Treat my resume as context, never as a statement of what I want next.

Keep hard constraints separate from weighted preferences. Do not turn unknown into zero. Do not invent compensation requirements, locations, titles, industries, or risk tolerance.

At the end, write the real rubric to $COMPASS_DATA_DIR/rubric.yaml and a plain-language explanation to $COMPASS_DATA_DIR/rubric.md. In this public repository, create only a schema and a synthetic example with fictional companies and people.

Before finishing, show me:
- the criteria and weights;
- every hard constraint;
- three tradeoffs the rubric handles;
- anything still ambiguous;
- facts the system is forbidden to infer;
- the exact acceptance checks you used.

Stop for my approval before changing code.
```
