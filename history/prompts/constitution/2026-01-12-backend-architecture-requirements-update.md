---
id: constitution-003
title: Backend Architecture Requirements Update
stage: constitution
date: 2026-01-12
surface: Updated project constitution to reflect detailed backend architecture requirements with JWT authentication and database integration
model: Qwen
feature: hackathon-todo-app
branch: main
user: user
command: /sp.constitution
labels: [constitution, hackathon, todo-app, phase-II, backend, architecture]
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


/sp.constitution # ROLE: Senior Python Backend Architect & API Designer
**Your Duty:** Build a complete, production-ready Python FastAPI backend server for the "Evolution of Todo" application, using **Spec-Driven Development** with Spec-Kit.

**PROJECT MANDATE (From Hackathon Document):**
- **Tech Stack:** Python FastAPI, SQLModel (ORM), JWT-based Authentication.
- **Core Deliverable:** Create a RESTful API that the existing Next.js frontend can connect to.
- **Critical Requirement:** You **MUST NOT** write any code manually. Refine the spec until Claude Code/Qwen generates the correct output.

**BACKEND SPECIFICATION:**

**1. API ENDPOINTS (Exactly as per Document):**
The backend must expose these endpoints at `http://localhost:8000`:
- `GET    /api/{user_id}/tasks` - List all tasks for a user.
- `POST   /api/{user_id}/tasks` - Create a new task for a user.
- `GET    /api/{user_id}/tasks/{task_id}` - Get a single task's details.
- `PUT    /api/{user_id}/tasks/{task_id}` - Update a task's title/description.
- `DELETE /api/{user_id}/tasks/{task_id}` - Delete a task.
- `PATCH  /api/{user_id}/tasks/{task_id}/complete` - Toggle a task's completion status.

**2. DATA MODELS (Using SQLModel):**
- Define a `Task` SQLModel with fields: `id`, `title`, `description`, `completed`, `user_id`, `created_at`, `updated_at`.
- Ensure `user_id` is a foreign key linking to the users table (managed by Better Auth).

**3. AUTHENTICATION FLOW (JWT Integration - as per Document):**
- The frontend will use Better Auth and send a JWT token in the `Authorization: Bearer <token>` header[citation:2].
- Your FastAPI backend must have middleware or dependency to **verify this JWT token** and extract the `user_id` from it[citation:2].
- **Security Rule:** Every API request must validate the token. The `user_id` from the token MUST match the `user_id` in the endpoint path. This ensures users can only access their own tasks[citation:2].

**4. DATABASE INTEGRATION:**
- Use SQLModel for all database operations.
- Prepare the connection to use a **Neon PostgreSQL** database (we will set up the actual database in the next step).
- Include database migration setup (using Alembic).

**5. MONOREPO STRUCTURE (As per Document's Spec-Kit Guide):**
Create this folder structure inside the main project:

/sp.constitution  
**YOUR TASK:** Using Spec-Driven Development, create the complete backend implementation. Start by generating the necessary specification files (`/specs/api/`, `/specs/database/`) and then have the AI generate all the code.

## Response snapshot

Updated the constitution file to reflect the detailed requirements for building the Python FastAPI backend, including specific API endpoints, data models, JWT authentication flow, and database integration requirements. The constitution now clearly specifies the backend architecture requirements for the "Evolution of Todo" application.

## Outcome

- ✅ Impact: Updated constitution to reflect detailed backend architecture requirements
- 🧪 Tests: Manual validation
- 📁 Files: 1 file updated (.specify/memory/constitution.md)
- 🔁 Next prompts: Plan and spec creation for backend implementation
- 🧠 Reflection: Constitution now includes all necessary backend architecture details

## Evaluation notes (flywheel)

- Failure modes observed: Bash script not available on Windows system
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): Standard constitution update with detailed backend requirements
- Next experiment (smallest change to try): Create implementation plan based on updated constitution