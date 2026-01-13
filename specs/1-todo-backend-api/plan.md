# Implementation Plan: Todo Backend API

**Feature**: 1-todo-backend-api  
**Created**: 2026-01-12  
**Status**: Ready for Implementation  
**Tech Stack**: Python 3.11+, FastAPI, SQLModel, PostgreSQL (Neon), JWT, Bcrypt, Passlib

## Architecture

### Tech Stack
- **Framework**: FastAPI (v0.104.1+)
- **ORM**: SQLModel (v0.0.18+)
- **Database**: PostgreSQL (Neon)
- **Authentication**: JWT with Bcrypt/Passlib
- **Environment**: Python 3.11+
- **ASGI Server**: Uvicorn

### Project Structure
```
backend/
├── main.py              # FastAPI application entry point
├── database.py          # Database connection and session management
├── models.py           # SQLModel database models
├── routes/
│   ├── __init__.py     # Routes package initialization
│   ├── tasks.py        # Task-related API endpoints
│   └── auth.py         # Authentication-related API endpoints
├── dependencies.py     # FastAPI dependency injection functions
└── requirements.txt    # Python dependencies
```

### Database Schema
- **User Table**: id, email, username, hashed_password, is_active, timestamps
- **Task Table**: id, title, description, completed, user_id (FK), timestamps

## Implementation Phases

### Phase 1: Project Setup
1. Create project structure
2. Define requirements.txt with all dependencies
3. Set up basic FastAPI application in main.py
4. Configure CORS middleware for frontend integration

### Phase 2: Database Layer
1. Implement database connection in database.py
2. Create SQLModel models in models.py
3. Set up async session management
4. Test database connectivity

### Phase 3: Authentication System
1. Implement JWT token utilities in dependencies.py
2. Create auth routes in routes/auth.py
3. Implement password hashing with Bcrypt/Passlib
4. Test authentication endpoints

### Phase 4: Task Management API
1. Create task routes in routes/tasks.py
2. Implement all 6 required endpoints:
   - POST `/api/{user_id}/tasks` - Create task
   - GET `/api/{user_id}/tasks` - Get all user tasks
   - GET `/api/{user_id}/tasks/{id}` - Get specific task
   - PUT `/api/{user_id}/tasks/{id}` - Update task
   - DELETE `/api/{user_id}/tasks/{id}` - Delete task
   - PATCH `/api/{user_id}/tasks/{id}/complete` - Toggle completion
3. Add proper authentication checks
4. Implement input validation with Pydantic schemas

### Phase 5: Integration & Testing
1. Test all endpoints with proper authentication
2. Verify data isolation between users
3. Test error handling and edge cases
4. Verify CORS configuration works with frontend

## File Dependencies
- main.py depends on: database.py, models.py, routes/
- database.py depends on: models.py
- routes/tasks.py depends on: models.py, dependencies.py, database.py
- routes/auth.py depends on: models.py, dependencies.py, database.py

## Success Criteria
- All 6 API endpoints are functional with proper authentication
- Database operations work correctly with Neon PostgreSQL
- JWT authentication properly validates tokens
- Users can only access their own tasks
- Application starts without errors on port 8000
- CORS allows requests from localhost:3000
- Input validation works for all endpoints