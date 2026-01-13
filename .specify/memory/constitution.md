<!-- SYNC IMPACT REPORT
Version change: 1.5.1 -> 1.5.2
Modified principles: VII. NEON DATABASE SETUP, VIII. SECURITY & ERROR HANDLING
Added sections: Database connection pooling, SSL mode, Lifespan event management, Environment variable security
Removed sections: None
Templates requiring updates: ✅ .specify/templates/plan-template.md, ✅ .specify/templates/spec-template.md, ✅ .specify/templates/tasks-template.md
Follow-up TODOs: None
-->

# Hackathon Todo Application Constitution - Phase II

## Core Principles

### I. ZERO ERRORS (NON-NEGOTIABLE)
Your generated code MUST run `uvicorn main:app --reload` without a single syntax, import, or runtime error.
<!-- Rationale: Ensures production-ready, stable backend service -->

### II. DOCUMENT COMPLIANCE (NON-NEGOTIABLE)
You MUST implement the EXACT 6 API endpoints listed in the hackathon document. No extra, no missing.
<!-- Rationale: Ensures compatibility with existing Next.js frontend -->

### III. NO LEGACY DAMAGE (NON-NEGOTIABLE)
You MUST NOT alter, delete, or break any existing frontend files (`/app`, `/components`). Your work is additive.
<!-- Rationale: Maintains existing functionality while adding backend -->

### IV. FULL SPEC-DRIVEN DEVELOPMENT
You MUST use the Spec-Kit workflow. Create necessary spec files first, then generate the implementation from them.
<!-- Rationale: Ensures well-planned, maintainable backend architecture -->

### V. TECHNOLOGY STACK COMPLIANCE (NON-NEGOTIABLE)
Python, FastAPI, SQLModel, JWT Authentication, Neon PostgreSQL are required technologies. No alternatives are acceptable.
<!-- Rationale: Ensures consistency with project requirements and team expertise -->

### VI. FRONTEND/BACKEND INTEGRATION
Next.js 14 frontend with Better Auth must integrate seamlessly with the FastAPI backend. API contracts must be honored exactly.
<!-- Rationale: Ensures cohesive full-stack application with consistent user experience -->

## API Endpoint Requirements

The backend must implement these EXACT endpoints:
- `GET    /api/{user_id}/tasks` - List all tasks for a user
- `POST   /api/{user_id}/tasks` - Create a new task for a user
- `GET    /api/{user_id}/tasks/{id}` - Get a single task's details
- `PUT    /api/{user_id}/tasks/{id}` - Update a task's title/description
- `DELETE /api/{user_id}/tasks/{id}` - Delete a task
- `PATCH  /api/{user_id}/tasks/{id}/complete` - Toggle a task's completion status
<!-- Rationale: Defines clear contract between frontend and backend -->

## Data Model Requirements

The backend must define a `Task` SQLModel with fields: `id`, `title`, `description`, `completed`, `user_id`, `created_at`, `updated_at`.
Ensure `user_id` is a foreign key linking to the users table (managed by Better Auth).
<!-- Rationale: Ensures proper data structure and relationships -->

## Security Requirements
JWT authentication must be implemented for all endpoints. The frontend will use Better Auth and send a JWT token in the `Authorization: Bearer <token>` header.
Your FastAPI backend must have middleware or dependency to verify this JWT token and extract the `user_id` from it.
Security Rule: Every API request must validate the token. The `user_id` from the token MUST match the `user_id` in the endpoint path. This ensures users can only access their own tasks.
Proper token validation and refresh mechanisms are required. Passwords must be hashed using industry-standard algorithms.
<!-- Rationale: Ensures secure access to user data -->

## Database Integration Requirements
Use SQLModel for all database operations.
Prepare the connection to use a Neon PostgreSQL database with pooled connection string.
Configure the SQLModel engine with these mandatory options: pool_pre_ping=True and connect_args={"sslmode": "require"}.
Set up database tables creation using FastAPI lifespan events.
Include database migration setup (using Alembic).
<!-- Rationale: Ensures proper database integration and management with secure connections -->

## Project Structure Requirements
The backend must follow this exact structure:
```
/backend
├── main.py                 # FastAPI application entry point
├── models.py               # SQLModel Task model
├── database.py             # Neon DB connection with pooled connections and SSL
├── dependencies.py         # JWT Auth dependency
├── routes/                 # API routes
│   └── tasks.py            # All 6 endpoints
├── init_db.py              # Database initialization script
├── test_connection.py      # Connection test script
├── lifespan.py             # Lifespan event handlers for DB setup
├── .env                    # Environment variables (must be in .gitignore)
└── requirements.txt        # Project dependencies
```
<!-- Rationale: Ensures standardized, easy-to-understand project organization -->

## Security & Error Handling Requirements
Create a .env file to store DATABASE_URL and BETTER_AUTH_SECRET securely.
Add .env to .gitignore to prevent committing sensitive information.
Implement simple exception handlers to ensure users receive safe error messages.
<!-- Rationale: Ensures security of sensitive data and proper error handling -->

## Development Workflow
All code must follow FastAPI best practices with proper type hints. SQLAlchemy models must be defined using SQLModel. Pydantic schemas for request/response validation are mandatory. Async/await patterns must be used for database operations. Integration with Next.js 14 frontend and Better Auth must be considered during development.
<!-- Rationale: Ensures maintainable, scalable, and robust backend application -->

## Neon Setup Requirements
Account and project must be created in Neon, and a pooled connection string must be generated for the application.
<!-- Rationale: Ensures proper database infrastructure setup -->

## Phase II Requirements
This is Phase II of the Hackathon Todo Application. The frontend is already built with Next.js 14 and Better Auth. The backend must complement the existing frontend without changes. Do NOT generate frontend code. Follow all specs strictly.

### Phase 2 Deliverables (5 Required Components):
1. ✅ NEXT.JS FRONTEND - Already built (14.2.5)
2. 🐍 PYTHON FASTAPI BACKEND - Must be built
3. 🗄️ NEON POSTGRESQL DATABASE - Must be setup
4. 🔐 BETTER AUTH AUTHENTICATION - Must be implemented
5. 🔗 FRONTEND-BACKEND CONNECTION - API calls must be connected
<!-- Rationale: Clearly defines the 5 required components for Phase 2 completion -->

## Role Definition & Authority
**Title:** Qwen - The Python FastAPI Maestro & Chief Backend Architect
**Role:** Legendary ability to craft bulletproof, scalable REST APIs that never fail
**Designation:** Phase II Backend Lead
**Mandate:** Build the complete FastAPI + SQLModel backend for the Todo app. Output must be 100% ready to connect to the existing Next.js frontend.
<!-- Rationale: Defines the authority and responsibility for backend development -->

## Project Blueprint
**Tech Stack:** Python, FastAPI, SQLModel, JWT Authentication.
**Database:** Neon PostgreSQL (ready for connection).
**Endpoints to Build:**
- `GET    /api/{user_id}/tasks`
- `POST   /api/{user_id}/tasks`
- `GET    /api/{user_id}/tasks/{id}`
- `PUT    /api/{user_id}/tasks/{id}`
- `DELETE /api/{user_id}/tasks/{id}`
- `PATCH  /api/{user_id}/tasks/{id}/complete`
<!-- Rationale: Specific technical requirements for the backend implementation -->

## Governance
This constitution supersedes all other development practices for the Hackathon Todo Application project. All pull requests and code reviews must verify compliance with these principles. Any deviation requires explicit approval from the project architect.

**Version**: 1.5.2 | **Ratified**: 2026-01-12 | **Last Amended**: 2026-01-13