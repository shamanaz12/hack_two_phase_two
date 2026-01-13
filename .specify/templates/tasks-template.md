---

description: "Task list template for FastAPI Todo Backend implementation"
---

# Tasks: FastAPI Todo Backend

**Input**: Design documents from `/specs/backend-fastapi-todo/`
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

- [ ] T001 Create backend project structure per implementation plan
- [ ] T002 Initialize Python project with FastAPI, SQLModel, Pydantic, and JWT dependencies
- [ ] T003 [P] Configure linting and formatting tools (black, ruff, mypy)

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

Examples of foundational tasks (adjust based on your project):

- [ ] T004 Setup database schema and Neon PostgreSQL connection in backend/database.py
- [ ] T005 [P] Implement JWT authentication framework in backend/dependencies.py
- [ ] T006 [P] Setup API routing structure in backend/routes/tasks.py
- [ ] T007 Create base models/entities that all stories depend on (Task model in backend/models.py)
- [ ] T008 Configure error handling and logging infrastructure
- [ ] T009 Setup project dependencies in backend/requirements.txt

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - User Authentication and Task Management (Priority: P1) 🎯 MVP

**Goal**: Enable authenticated users to create and retrieve their tasks

**Independent Test**: Can be fully tested by making authenticated API requests to create and read tasks, delivering core functionality to end users

### Tests for User Story 1 (OPTIONAL - only if tests requested) ⚠️

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [ ] T011 [P] [US1] Contract test for POST /api/{user_id}/tasks in tests/test_api/test_tasks.py
- [ ] T012 [P] [US1] Contract test for GET /api/{user_id}/tasks in tests/test_api/test_tasks.py
- [ ] T013 [P] [US1] Integration test for task creation flow in tests/test_api/test_tasks.py

### Implementation for User Story 1

- [ ] T014 [P] [US1] Create Task model in backend/models.py
- [ ] T015 [P] [US1] Create Task schemas in backend/models.py
- [ ] T016 [US1] Implement task creation endpoint in backend/routes/tasks.py
- [ ] T017 [US1] Implement task retrieval endpoint in backend/routes/tasks.py
- [ ] T020 [US1] Add authentication middleware and validation
- [ ] T021 [US1] Add validation and error handling for task operations

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - Task Completion Toggle (Priority: P2)

**Goal**: Allow users to mark tasks as complete/incomplete

**Independent Test**: Can be tested by making PATCH requests to toggle task completion status, delivering the ability to update task state

### Tests for User Story 2 (OPTIONAL - only if tests requested) ⚠️

- [ ] T022 [P] [US2] Contract test for PATCH /api/{user_id}/tasks/{id}/complete in tests/test_api/test_tasks.py
- [ ] T023 [P] [US2] Integration test for task completion flow in tests/test_api/test_tasks.py

### Implementation for User Story 2

- [ ] T024 [P] [US2] Add completion toggle logic in backend/routes/tasks.py
- [ ] T025 [US2] Implement PATCH /api/{user_id}/tasks/{id}/complete endpoint
- [ ] T026 [US2] Add validation and error handling for completion toggle

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Individual Task Operations (Priority: P3)

**Goal**: Enable users to view, update, and delete specific tasks

**Independent Test**: Can be tested by making GET, PUT, and DELETE requests to individual task endpoints, delivering full CRUD functionality

### Tests for User Story 3 (OPTIONAL - only if tests requested) ⚠️

- [ ] T027 [P] [US3] Contract test for GET /api/{user_id}/tasks/{id} in tests/test_api/test_tasks.py
- [ ] T028 [P] [US3] Contract test for PUT /api/{user_id}/tasks/{id} in tests/test_api/test_tasks.py
- [ ] T029 [P] [US3] Contract test for DELETE /api/{user_id}/tasks/{id} in tests/test_api/test_tasks.py

### Implementation for User Story 3

- [ ] T030 [P] [US3] Implement GET /api/{user_id}/tasks/{id} endpoint in backend/routes/tasks.py
- [ ] T031 [US3] Implement PUT /api/{user_id}/tasks/{id} endpoint in backend/routes/tasks.py
- [ ] T032 [US3] Implement DELETE /api/{user_id}/tasks/{id} endpoint in backend/routes/tasks.py
- [ ] T033 [US3] Add validation and error handling for individual task operations

**Checkpoint**: All user stories should now be independently functional

---

## Phase 6: User Story 4 - Secure Data Isolation (Priority: P1)

**Goal**: Ensure users can only access their own tasks and not others' data

**Independent Test**: Can be tested by attempting to access another user's tasks with my token, delivering assurance that data isolation works correctly

### Tests for User Story 4 (OPTIONAL - only if tests requested) ⚠️

- [ ] T034 [P] [US4] Integration test for data isolation in tests/test_api/test_tasks.py
- [ ] T035 [P] [US4] Test for unauthorized access attempts in tests/test_api/test_tasks.py

### Implementation for User Story 4

- [ ] T036 [P] [US4] Add user ID validation in all endpoints to ensure data isolation
- [ ] T037 [US4] Implement proper authorization checks in backend/routes/tasks.py
- [ ] T038 [US4] Add comprehensive error handling for unauthorized access

**Checkpoint**: All user stories should now be secure and functional

---

## Phase N: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [ ] T039 [P] Documentation updates in README.md
- [ ] T040 Code cleanup and refactoring
- [ ] T041 Performance optimization across all endpoints
- [ ] T042 [P] Additional unit tests (if requested) in tests/unit/
- [ ] T043 Security hardening
- [ ] T044 Run quickstart validation
- [ ] T045 Ensure application starts with `uvicorn main:app --reload` without errors

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
- **User Story 2 (P2)**: Can start after Foundational (Phase 2) - May integrate with US1 but should be independently testable
- **User Story 3 (P3)**: Can start after Foundational (Phase 2) - May integrate with US1/US2 but should be independently testable
- **User Story 4 (P1)**: Can start after Foundational (Phase 2) - Integrates with all other stories

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
Task: "Contract test for POST /api/{user_id}/tasks in tests/test_api/test_tasks.py"
Task: "Contract test for GET /api/{user_id}/tasks in tests/test_api/test_tasks.py"

# Launch all models for User Story 1 together:
Task: "Create User model in backend/models/user.py"
Task: "Create Task model in backend/models/task.py"
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