---
id: constitution-001
title: Update Constitution for Phase II
stage: constitution
date: 2026-01-12
surface: Updated project constitution to reflect Phase II requirements for the Hackathon Todo Application
model: Qwen
feature: hackathon-todo-app
branch: main
user: user
command: /sp.constitution
labels: [constitution, hackathon, todo-app, phase-II]
links:
  spec: 
  ticket: 
  adr: 
  pr: 
files:
  - .specify/memory/constitution.md
tests:
  - constitution-validation: PASS
---

## Prompt

As the main request completes, you MUST create and complete a PHR (Prompt History Record) using agent‑native tools when possible.

1) Determine Stage
   - Stage: constitution | spec | plan | tasks | red | green | refactor | explainer | misc | general

2) Generate Title and Determine Routing:
   - Generate Title: 3–7 words (slug for filename)
   - Route is automatically determined by stage:
     - `constitution` → `history/prompts/constitution/`
     - Feature stages → `history/prompts/<feature-name>/` (spec, plan, tasks, red, green, refactor, explainer, misc)
     - `general` → `history/prompts/general/`

3) Create and Fill PHR (Shell first; fallback agent‑native)
   - Run: `.specify/scripts/bash/create-phr.sh --title "<title>" --stage <stage> [--feature <name>] --json`
   - Open the file and fill remaining placeholders (YAML + body), embedding full PROMPT_TEXT (verbatim) and concise RESPONSE_TEXT.
   - If the script fails:
     - Read `.specify/templates/phr-template.prompt.md` (or `templates/…`)
     - Allocate an ID; compute the output path based on stage from step 2; write the file
     - Fill placeholders and embed full PROMPT_TEXT and concise RESPONSE_TEXT

4) Validate + report
   - No unresolved placeholders; path under `history/prompts/` and matches stage; stage/title/date coherent; print ID + path + stage + title.
   - On failure: warn, don't block. Skip only for `/sp.phr`.

/sp.constitution You are working on Phase II of a Hackathon Todo Application.
Frontend is built with Next.js 14 and uses Better Auth for authentication.
Backend is a Python FastAPI service.
Database is Neon Serverless PostgreSQL.
Specs are managed using GitHub Spec-Kit Plus.
Do NOT generate frontend code.
Follow all specs strictly.

## Response snapshot

Updated the constitution file to reflect Phase II requirements for the Hackathon Todo Application, incorporating information about the existing Next.js 14 frontend with Better Auth, and emphasizing the backend focus with FastAPI and Neon PostgreSQL.

## Outcome

- ✅ Impact: Updated constitution to reflect Phase II requirements
- 🧪 Tests: Manual validation
- 📁 Files: 1 file updated (.specify/memory/constitution.md)
- 🔁 Next prompts: Plan and spec creation for backend implementation
- 🧠 Reflection: Constitution now properly reflects the project's current state and requirements

## Evaluation notes (flywheel)

- Failure modes observed: Bash script not available on Windows system
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): Standard constitution update
- Next experiment (smallest change to try): Create implementation plan based on updated constitution