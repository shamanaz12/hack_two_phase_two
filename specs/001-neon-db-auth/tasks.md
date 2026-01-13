---

description: "Task list for Neon PostgreSQL Database & Better Auth Integration implementation"
---

# Tasks: Neon PostgreSQL Database & Better Auth Integration

**Input**: Design documents from `/specs/001-neon-db-auth/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: The examples below include test tasks. Tests are OPTIONAL - only include them if explicitly requested in the feature specification.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- **Web app**: `backend/src/`, `frontend/src/`
- **Mobile**: `api/src/`, `ios/src/` or `android/src/`
- Paths shown below assume single project - adjust based on plan.md structure

<!--
  ============================================================================
  IMPORTANT: The tasks below are SAMPLE TASKS for illustration purposes only.

  The /sp.tasks command MUST replace these with actual tasks based on:
  - User stories from spec.md (with their priorities P1, P2, P3...)
  - Feature requirements from plan.md
  - Entities from data-model.md
  - Endpoints from contracts/

  Tasks MUST be organized by user story so each story can be:
  - Implemented independently
  - Tested independently
  - Delivered as an MVP increment

  DO NOT keep these sample tasks in the generated tasks.md file.
  ============================================================================
-->

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [X] T001 Create backend project structure per implementation plan
- [X] T002 Initialize Python project with FastAPI, SQLModel, Pydantic, and JWT dependencies
- [X] T003 [P] Configure linting and formatting tools (black, ruff, mypy)

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

Examples of foundational tasks (adjust based on your project):

- [X] T004 Setup database schema and Neon PostgreSQL connection in backend/database.py
- [X] T005 [P] Implement JWT authentication framework in backend/dependencies.py
- [X] T006 [P] Setup API routing structure in backend/routes/tasks.py
- [X] T007 Create base models/entities that all stories depend on (Task model in backend/models.py)
- [X] T008 Configure error handling and logging infrastructure
- [X] T009 Setup project dependencies in backend/requirements.txt

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Secure API Access (Priority: P1) 🎯 MVP

**Goal**: Enable authenticated users to make API requests with JWT tokens

**Independent Test**: Can be fully tested by obtaining a JWT token from Better Auth, making API requests with the token, and verifying that only authorized requests succeed, delivering core security functionality to end users

### Tests for User Story 1 (OPTIONAL - only if tests requested) ⚠️

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [X] T010 [P] [US1] Contract test for JWT token validation in tests/test_api/test_auth.py
- [X] T011 [P] [US1] Contract test for unauthorized access rejection in tests/test_api/test_auth.py
- [X] T012 [P] [US1] Integration test for token verification flow in tests/test_api/test_auth.py

### Implementation for User Story 1

- [X] T013 [P] [US1] Create User and Task models in backend/models.py
- [X] T014 [P] [US1] Create JWT token schemas in backend/models.py
- [X] T015 [US1] Implement JWT verification dependency in backend/dependencies.py
- [X] T016 [US1] Add JWT validation to all task endpoints in backend/routes/tasks.py
- [X] T017 [US1] Add validation and error handling for authentication

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - Data Isolation (Priority: P1)

**Goal**: Ensure users can only access their own tasks and not others' data

**Independent Test**: Can be tested by attempting to access another user's tasks with my token, delivering assurance that data isolation works correctly

### Tests for User Story 2 (OPTIONAL - only if tests requested) ⚠️

- [X] T018 [P] [US2] Contract test for user ID comparison in tests/test_api/test_auth.py
- [X] T019 [P] [US2] Integration test for data isolation flow in tests/test_api/test_auth.py

### Implementation for User Story 2

- [X] T020 [P] [US2] Add user ID verification function in backend/dependencies.py
- [X] T021 [US2] Implement user ID validation in all task endpoints in backend/routes/tasks.py
- [X] T022 [US2] Add database query filtering by user ID in backend/routes/tasks.py
- [X] T023 [US2] Add validation and error handling for data isolation

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Token Verification (Priority: P2)

**Goal**: Verify JWT tokens using the same secret as Better Auth

**Independent Test**: Can be tested by verifying that tokens issued by Better Auth are accepted while forged tokens are rejected, delivering trust in the authentication system

### Tests for User Story 3 (OPTIONAL - only if tests requested) ⚠️

- [X] T024 [P] [US3] Contract test for token signature verification in tests/test_api/test_auth.py
- [X] T025 [P] [US3] Integration test for token validation flow in tests/test_api/test_auth.py

### Implementation for User Story 3

- [X] T026 [P] [US3] Configure shared secret handling in backend/dependencies.py
- [X] T027 [US3] Implement token signature verification in backend/dependencies.py
- [X] T028 [US3] Add token validation to all endpoints in backend/routes/tasks.py
- [X] T029 [US3] Add validation and error handling for token verification

**Checkpoint**: All user stories should now be independently functional

---

## Phase 6: User Story 4 - Seamless Authentication Flow (Priority: P2)

**Goal**: Automatically include JWT tokens with API requests from the frontend

**Independent Test**: Can be tested by logging in, performing various task operations, and verifying that requests are automatically authenticated, delivering frictionless user experience

### Tests for User Story 4 (OPTIONAL - only if tests requested) ⚠️

- [X] T030 [P] [US4] Contract test for automatic token attachment in tests/test_api/test_client.py
- [X] T031 [P] [US4] Integration test for seamless authentication flow in tests/test_api/test_client.py

### Implementation for User Story 4

- [X] T032 [P] [US4] Update API client to automatically attach JWT tokens in lib/api.ts
- [X] T033 [US4] Implement token retrieval from Better Auth in lib/api.ts
- [X] T034 [US4] Add token refresh mechanism in lib/api.ts
- [X] T035 [US4] Add validation and error handling for client-side authentication

**Checkpoint**: All user stories should now be secure and functional

---

## Phase N: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [X] T036 [P] Documentation updates in README.md
- [X] T037 Code cleanup and refactoring
- [X] T038 Performance optimization across all endpoints
- [X] T039 [P] Additional unit tests (if requested) in tests/unit/
- [X] T040 Security hardening
- [X] T041 Run quickstart validation
- [X] T042 Ensure application starts with `uvicorn main:app --reload` without errors

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P1)**: Can start after Foundational (Phase 2) - May integrate with US1 but should be independently testable
- **User Story 3 (P2)**: Can start after Foundational (Phase 2) - May integrate with US1/US2 but should be independently testable
- **User Story 4 (P2)**: Can start after Foundational (Phase 2) - Integrates with all other stories

### Within Each User Story

- Tests (if included) MUST be written and FAIL before implementation
- Models before services
- Services before endpoints
- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, all user stories can start in parallel (if team capacity allows)
- All tests for a user story marked [P] can run in parallel
- Models within a story marked [P] can run in parallel
- Different user stories can be worked on in parallel by different team members

---

## Parallel Example: User Story 1

```bash
# Launch all tests for User Story 1 together (if tests requested):
Task: "Contract test for JWT token validation in tests/test_api/test_auth.py"
Task: "Contract test for unauthorized access rejection in tests/test_api/test_auth.py"

# Launch all models for User Story 1 together:
Task: "Create User model in backend/models.py"
Task: "Create Task model in backend/models.py"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test User Story 1 independently
5. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (MVP!)
3. Add User Story 2 → Test independently → Deploy/Demo
4. Add User Story 3 → Test independently → Deploy/Demo
5. Add User Story 4 → Test independently → Deploy/Demo
6. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1
   - Developer B: User Story 2
   - Developer C: User Story 3
   - Developer D: User Story 4
3. Stories complete and integrate independently

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Verify tests fail before implementing
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence