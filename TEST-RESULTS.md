# DemoBuddy test evidence

## Result
**15 / 15 automated browser checks passed** on 2026-10-12 using Chromium and Python Playwright against the local HTML prototype.

## Checks
1. Page loads and has the expected title.
2. Default sample project appears.
3. Sample session starts in Hackathon Judge mode.
4. Hint control adds a hint message.
5. Demo Rescue control adds a rescue plan.
6. Three-answer flow reaches the final pitch report.
7. Three user answers are retained in the visible session.
8. Final clarity score is visible.
9. Recruiter mode can start.
10. Recruiter mode uses its custom first question.
11. Empty-answer guard prevents blank submission.
12. Mobile viewport has no horizontal overflow.
13. Short answer triggers a clarifying follow-up.
14. Technical answer triggers a trade-off follow-up.
15. No uncaught browser JavaScript errors were detected.

## Evidence files
- `evidence-home.png`: setup screen.
- `evidence-report-panel.png`: completed rehearsal and pitch report.
- `demobuddy-cover.png`: article cover image.

## Scope and limitations
This is a rules-based browser prototype, not a hosted LLM-backed agent. It does not use AWS services or send data to a server. The score is a transparent heuristic and not a validated assessment. Browser tests verify expected interactions; they do not prove that real users enjoy the product. Public hosting and user testing are still outstanding.
