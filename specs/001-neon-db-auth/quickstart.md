# Quickstart Guide: Neon PostgreSQL & Better Auth Integration

**Feature**: Neon PostgreSQL Database & Better Auth Integration
**Date**: 2026-01-12
**Author**: Qwen - The Cloud Database Wizard & Infrastructure Sorcerer

## Overview

This guide provides step-by-step instructions to set up the Neon PostgreSQL database and integrate Better Auth with JWT verification for the Todo application backend.

## Prerequisites

- Python 3.11+
- pip package manager
- Git
- A Neon.tech account
- Better Auth configured in the frontend

## Step 1: Set Up Neon PostgreSQL

### 1.1 Create a Neon Account
1. Visit [https://neon.tech](https://neon.tech)
2. Click "Get Started for Free"
3. Sign up with your preferred method (Google, GitHub, or email)

### 1.2 Create a Project
1. After logging in, click "New Project"
2. Enter a project name (e.g., "todo-app")
3. Select a region closest to your users
4. Choose the free plan option
5. Click "Create Project"

### 1.3 Get Connection Details
1. In your project dashboard, go to the "Connection Details" section
2. Note the connection string, which will look like:
   ```
   postgresql://username:password@ep-cool-cloud-123.us-east-1.aws.neon.tech/dbname
   ```
3. Save this connection string for later use

## Step 2: Configure Backend Environment

### 2.1 Create Environment File
1. Navigate to the `/backend` directory
2. Create a `.env` file:
   ```bash
   cd backend
   touch .env
   ```

### 2.2 Add Database Credentials
1. Open the `.env` file in a text editor
2. Add your Neon connection string:
   ```
   DATABASE_URL=postgresql://username:password@ep-cool-cloud-123.us-east-1.aws.neon.tech/dbname
   ```
3. Add the Better Auth secret (shared with frontend):
   ```
   BETTER_AUTH_SECRET=your_better_auth_secret_here
   ```

### 2.3 Update database.py
Ensure your `backend/database.py` file reads the environment variable:

```python
from sqlmodel import create_engine
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
import os

# Get database URL from environment
DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("DATABASE_URL environment variable is not set. Please configure your .env file.")

# Create async engine for async operations with SSL configuration
engine = create_async_engine(
    DATABASE_URL,
    echo=True,
    pool_pre_ping=True,
    connect_args={"sslmode": "require"}
)

# Create async session maker
AsyncSessionLocal = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
```

## Step 3: Implement JWT Verification

### 3.1 Update dependencies.py
Create or update the JWT verification dependency in `backend/dependencies.py`:

```python
from fastapi import HTTPException, status, Request, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from typing import Dict, Optional
import jwt
from passlib.context import CryptContext
import os
from datetime import datetime, timedelta
import uuid

# Initialize password hashing context
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Get secret key from environment
SECRET_KEY = os.getenv("BETTER_AUTH_SECRET", "fallback-secret-key-change-in-production")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

security = HTTPBearer()

def verify_token(token: str) -> dict:
    """Verify a JWT token and return its payload."""
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except jwt.PyJWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )

def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)):
    """Dependency to get current user from JWT token"""
    try:
        token = credentials.credentials
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id: str = payload.get("sub")  # Using 'sub' field as user ID
        if user_id is None:
            raise HTTPException(status_code=401, detail="Invalid token")
        return {"user_id": user_id}
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token has expired")
    except jwt.JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

def verify_user_access(path_user_id: str, current_user: dict):
    """Verify that the user_id in the path matches the user_id in the token"""
    token_user_id = current_user.get("user_id")
    if not token_user_id or str(token_user_id) != path_user_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Access denied: User ID mismatch"
        )
```

## Step 4: Apply Authentication to Endpoints

### 4.1 Update routes/tasks.py
Apply the authentication dependency to all task endpoints in `backend/routes/tasks.py`:

```python
from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from sqlmodel import select
from backend.database import AsyncSessionLocal
from backend.models import Task, TaskCreate, TaskRead, TaskUpdate
from backend.dependencies import get_current_user, verify_user_access
from uuid import UUID
import uuid

router = APIRouter()

@router.post("/tasks", response_model=TaskRead, status_code=status.HTTP_201_CREATED)
async def create_task(
    user_id: str, 
    task_data: TaskCreate, 
    current_user: dict = Depends(get_current_user)
):
    # Verify that the user_id in the path matches the token
    verify_user_access(user_id, current_user)
    
    # Verify that the user_id is a valid UUID
    try:
        user_uuid = uuid.UUID(user_id)
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid user ID format")

    async with AsyncSessionLocal() as session:
        # Create a new task
        db_task = Task(
            title=task_data.title,
            description=task_data.description,
            user_id=user_uuid
        )

        session.add(db_task)
        await session.commit()
        await session.refresh(db_task)

        return db_task

@router.get("/tasks", response_model=List[TaskRead])
async def get_tasks(
    user_id: str, 
    current_user: dict = Depends(get_current_user)
):
    # Verify that the user_id in the path matches the token
    verify_user_access(user_id, current_user)
    
    # Verify that the user_id is a valid UUID
    try:
        user_uuid = uuid.UUID(user_id)
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid user ID format")

    async with AsyncSessionLocal() as session:
        # Query tasks for the specific user
        statement = select(Task).where(Task.user_id == user_uuid)
        result = await session.execute(statement)
        tasks = result.scalars().all()

        return tasks

# Similar authentication should be applied to other endpoints:
# - get_task
# - update_task
# - delete_task
# - toggle_task_completion
```

## Step 5: Initialize Database Tables

### 5.1 Run Database Initialization
1. Make sure your environment is set up with the correct `DATABASE_URL`
2. Run the database initialization script:
   ```bash
   python backend/init_db.py
   ```

### 5.2 Test the Connection
1. Run the connection test script:
   ```bash
   python backend/test_connection.py
   ```

## Step 6: Start the Backend Server

1. Install dependencies:
   ```bash
   pip install -r backend/requirements.txt
   ```

2. Start the server:
   ```bash
   cd backend
   uvicorn main:app --reload
   ```

## Verification Steps

1. Verify the database connection by checking that the tables were created in your Neon dashboard
2. Test the authentication by making requests with and without valid JWT tokens
3. Verify that user ID validation works by attempting to access another user's tasks
4. Confirm that all 6 required API endpoints are functioning correctly

## Troubleshooting

### Common Issues

- **SSL Connection Error**: Ensure your database connection includes SSL configuration
- **JWT Validation Error**: Verify that the `BETTER_AUTH_SECRET` matches between frontend and backend
- **User ID Mismatch Error**: Check that the user ID in the JWT token matches the user ID in the API endpoint path
- **Environment Variables Not Loading**: Make sure the `.env` file is in the correct location and properly formatted

### Useful Commands

- Check if environment variables are loaded:
  ```python
  import os
  print(os.getenv("DATABASE_URL"))
  print(os.getenv("BETTER_AUTH_SECRET"))
  ```

- Test database connection directly:
  ```bash
  python -c "from backend.database import engine; print('Connected successfully')"
  ```