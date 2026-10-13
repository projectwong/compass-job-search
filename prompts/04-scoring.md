# Prompt 04 Score fit and confidence

```text
Implement scoring against the approved rubric without creating false precision.

Use this order:
1. evaluate hard constraints as pass, fail, or unknown;
2. calculate company fit and role fit separately from available evidence;
3. report coverage and confidence separately from fit;
4. leave current priority outside the fit calculation.

Every result must explain which evidence affected it, which criteria lack evidence, which evidence conflicts, and which rubric version was used. Do not let missing evidence act like a negative value. Do not invent a percentage unless the rubric mathematically supports it, and round output to a level justified by the inputs.

Write tests first for failed constraints, unknown constraints, missing evidence, conflicting evidence, zero-weight criteria, ties, and rubric-version changes. Add a sensitivity check that reports when small weight changes alter the top tier.

Demonstrate with synthetic companies only. Show the test results and three readable example explanations, then stop.
```
