# Title
DemoBuddy: A Tiny Rehearsal Agent That Adapts to You 🎤

# Description
Student projects deserve better demos. DemoBuddy is a browser-local rehearsal agent that helps students practise explaining a project through audience-specific questions, hints, friendly feedback, and a fallback plan for a failed live demo. I built a working rules-based prototype and tested its interaction flow across several scenarios.

# Body

## DemoBuddy: A Tiny Rehearsal Agent That Adapts to You 🎤

Have you ever built a project you were proud of, then struggled to explain it clearly during a college presentation, hackathon, or interview?

You know what your app does. But when someone asks why you chose a particular approach—or your live demo suddenly fails—it can be hard to find the right words.

That is the problem I wanted to explore with **DemoBuddy**, a small rehearsal agent for students and beginner developers. The goal is to make practice feel more like a supportive conversation than an exam.

## What it does and who it is for

DemoBuddy helps a student rehearse a project explanation before presenting to a real audience. The user enters a project name and short description, then chooses one of three audience modes: Curious Beginner, Recruiter, or Hackathon Judge.

Each mode starts with a different kind of question. A beginner asks what problem the project solves. A recruiter focuses on the work the developer personally did and its impact. A judge asks about differentiation, assumptions, and trade-offs.

The session has three questions, then generates a short pitch draft and a checklist of one strength and one next step.

## How I built the prototype

The first version is a static browser app built with **HTML, CSS, and vanilla JavaScript**. It does not require an account, store project notes on a server, or ask the student to deploy cloud resources just to try a rehearsal.

The interaction logic is rules-based. After an answer, the agent checks for signals such as answer length, references to users or outcomes, and mentions of technical choices. It then chooses a follow-up question. A short answer leads to a request for a concrete example; a technical answer leads to a question about the decision and its trade-off; a user-focused answer leads to a question about how to test the benefit.

I also added a **Need a hint?** control and a **Demo Rescue** mode. Rescue mode helps the presenter prepare an honest fallback—explain what failed, show a recording or screenshot if one exists, and name the next diagnostic step rather than pretending the demo worked.

**Tools used:** HTML, CSS, JavaScript, Chromium, and Python Playwright for browser acceptance tests. **AWS services / hosted AI model:** none are connected in this prototype yet. I kept the first build local rather than claiming an AWS or model integration that I had not configured and tested.

## The delightful detail: one question at a time

The most important UX choice was to avoid overwhelming a beginner with a long list of questions. DemoBuddy asks one question at a time, offers a hint without giving away the answer, and adapts its next question based on the response. At the end, the student gets a 60-second pitch draft based on their own notes.

The score is intentionally labelled as a simple clarity checklist—not as a judgement of project quality. That keeps the feedback more transparent and useful.

## How I know the prototype works

I ran **15 automated browser checks**, and all 15 passed. They covered the sample flow, hint action, Demo Rescue mode, completion of three questions, answer capture, final pitch generation, recruiter mode, empty-answer handling, mobile layout overflow, adaptive follow-up for a short answer, adaptive follow-up for a technical answer, and browser-console errors.

These are functional checks, not a human user study. I have not yet validated whether students find the experience enjoyable; the next test would be to ask a few students to complete a rehearsal and collect their feedback.

## Proof it works

I am attaching a screenshot of a completed rehearsal showing the conversation, the checklist, and the generated pitch. The source project is included with this submission package so the prototype can be opened locally and tried using the sample project.

## What I would improve next

The next stage would be testing with real students, refining the branching questions based on their feedback, and then evaluating whether a model-backed agent would add enough value to justify the extra setup. If I connect a hosted model or AWS services later, I will document and test that integration separately rather than imply it is already live.

**Your turn:** What would make you enjoy practising a project demo more—a friendly audience, hints when you get stuck, a realistic hackathon-judge mode, or an honest plan for when the live demo fails?

#agents #StudentBuilders #DeveloperTools #ProjectDemo
