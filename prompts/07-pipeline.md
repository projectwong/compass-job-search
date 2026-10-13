# Prompt 07 Track opportunities and conversations

```text
Add opportunity and conversation workflows without automating applications or outreach.

An opportunity belongs to one company and has a role title, source URL, discovered date, state, work model, location, fit assessment, contacts, stage history, decision, and exactly one next action while active. Planned actions do not count as completed application dates.

Create commands and templates for:
- adding an opportunity;
- moving it through identified, applied, screening, interviewing, offer, and closed states;
- preparing a conversation brief;
- recording conversation notes and commitments;
- scheduling a dated follow-up.

The system may draft text into a file, but it must not send a message, submit a form, or open an authenticated site. Treat every generated statement about a company or person as a draft until supported by evidence.

Write tests for invalid transitions, an active opportunity with no next action, several roles at one company, closing with history preserved, and commitments without dates. Demonstrate with synthetic data and stop.
```
