---
id: constitution-002
title: Phase 2 Requirements Update
stage: constitution
date: 2026-01-12
surface: Updated project constitution to reflect Phase 2 requirements with 5 specific deliverables
model: Qwen
feature: hackathon-todo-app
branch: main
user: user
command: /sp.constitution
labels: [constitution, hackathon, todo-app, phase-II, backend]
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


/sp.constitution PHASE 2 MEIN TUMHE YE 5 CHEEZEN BANANI HAIN:

✅ NEXT.JS FRONTEND - Tumne bana liya (14.2.5)

🐍 PYTHON FASTAPI BACKEND - Abhi banana hai

🗄️ NEON POSTGRESQL DATABASE - Setup karna hai

🔐 BETTER AUTH AUTHENTICATION - Implement karna hai

🔗 FRONTEND-BACKEND CONNECTION - API calls connect karni hain

## Response snapshot

Updated the constitution file to reflect the specific requirements for Phase 2 of the Hackathon Todo Application, clearly outlining the 5 required deliverables. The frontend is already completed with Next.js 14.2.5, and the backend needs to be built with Python FastAPI, Neon PostgreSQL database setup, Better Auth authentication implementation, and connecting the frontend-backend API calls.

## Outcome

- ✅ Impact: Updated constitution to reflect specific Phase 2 requirements
- 🧪 Tests: Manual validation
- 📁 Files: 1 file updated (.specify/memory/constitution.md)
- 🔁 Next prompts: Plan and spec creation for backend implementation
- 🧠 Reflection: Constitution now clearly defines all 5 deliverables for Phase 2

## Evaluation notes (flywheel)

- Failure modes observed: Bash script not available on Windows system
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): Standard constitution update with specific requirements
- Next experiment (smallest change to try): Create implementation plan based on updated constitution