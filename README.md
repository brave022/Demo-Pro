# DemoBuddy — Interactive Project Rehearsal Agent

DemoBuddy is a browser-local, interactive rehearsal agent for students and developers practising project presentations. It helps presenters overcome stage fright, refine their value proposition, and prepare an honest fallback plan for live demo failures.

## Features
- **Adaptive Audience Modes**: Curious Beginner, Recruiter, Hackathon Judge, Angel/VC Investor, and Senior Tech Architect.
- **Voice Coach & Dictation (Web Speech API)**:
  - 🔊 **Voice Coach**: Listens to DemoBuddy ask questions and share feedback aloud with natural speech cadence.
  - 🎤 **Voice Dictation**: Practise speaking answers verbally directly into the microphone.
  - 🎵 **Web Audio Chimes**: Gentle audio feedback for questions and milestone completions.
- **Live Rehearsal Timer**: Active countdown timer with pause/resume and pacing prompts.
- **Quick Project Templates**: One-click load for sample projects (Campus Event Finder, MediScan AI, EcoTrack IoT, CodeReview Buddy).
- **Interactive Demo Rescue Arsenal**: Dedicated emergency scripts and graceful fallback plans for 500 errors, stage WiFi loss, auth glitches, and UI lag.
- **Pitch Tuner (Tone Switcher)**: Generates a 60-second pitch draft with one-click toggles for 30s Punchy Elevator Pitch, Default Narrative, or Deep Technical Architecture breakdown.
- **Multi-Dimensional Clarity Scorecard**: Visual sub-scores for Problem Clarity, Technical Depth, and Demo Resilience, along with filler word detection.
- **Export & History**:
  - Download full rehearsal transcript as Markdown (`.md`).
  - Print / Save as PDF with clean formatting.
  - Local rehearsal history with progress tracking across practice sessions.
- **Dark & Light Modes**: Choose between classic Warm Paper theme and Midnight Dark mode.

## Run it
1. Open `index.html` in any modern web browser (Edge, Chrome, Firefox, Safari).
2. Click **Try the sample project** for a guided walkthrough, or select a **Quick Template** / enter your own project details.
3. Click **Meet my audience →** to enter the rehearsal room.

A local static server also works (`npx serve .` or Python `python -m http.server`), but no installation is required.

## Testing & Quality Assurance
- Automated end-to-end tests: `python test_app.py`
- Test suite validates 15/15 checks (UI elements, adaptive branching, recruiter mode, mobile responsiveness, error guards, and console health).

## Privacy Note
DemoBuddy runs 100% locally in your browser. All project descriptions, speech dictation, and rehearsal notes stay strictly on your device.
