# Data Model: Neon PostgreSQL Database & Better Auth Integration

**Feature**: Neon PostgreSQL Database & Better Auth Integration
**Date**: 2026-01-12
**Author**: Qwen - The Cloud Database Wizard & Infrastructure Sorcerer

## Entity Definitions

### User
Represents a registered user with authentication credentials and profile information.

- **Fields**:
  - `id` (UUID): Unique identifier for the user
  - `email` (String): User's email address (unique, indexed)
  - `username` (String): User's chosen username (unique, indexed)
  - `hashed_password` (String): BCrypt hashed password
  - `is_active` (Boolean): Whether the account is active (default: true)
  - `created_at` (DateTime): Timestamp of account creation
  - `updated_at` (DateTime): Timestamp of last update

- **Relationships**:
  - One-to-many with Task (user has many tasks)

- **Validation**:
  - Email must be valid email format
  - Username must be unique
  - Password must meet minimum strength requirements

### Task
Represents a todo item with title, description, completion status, and user relationship.

- **Fields**:
  - `id` (UUID): Unique identifier for the task
  - `title` (String): Task title (required)
  - `description` (String): Optional task description
  - `completed` (Boolean): Whether the task is completed (default: false)
  - `user_id` (UUID): Foreign key linking to User
  - `created_at` (DateTime): Timestamp of task creation
  - `updated_at` (DateTime): Timestamp of last update

- **Relationships**:
  - Many-to-one with User (task belongs to one user)

- **Validation**:
  - Title must not be empty
  - User_id must reference an existing user

### JWT Token
Represents a secure authentication token containing user identity and permissions.

- **Fields**:
  - `token` (String): The JWT token string
  - `user_id` (UUID): The user ID contained in the token payload
  - `expires_at` (DateTime): Expiration timestamp
  - `issued_at` (DateTime): Issue timestamp

- **State Transitions**:
  - Valid → Expired (when current time exceeds expires_at)
  - Valid → Revoked (when manually invalidated)

## Database Schema

### SQL Tables

#### users table
```sql
CREATE TABLE users (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    email VARCHAR(255) UNIQUE NOT NULL,
    username VARCHAR(255) UNIQUE NOT NULL,
    hashed_password VARCHAR(255) NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

CREATE INDEX idx_users_email ON users(email);
CREATE INDEX idx_users_username ON users(username);
```

#### tasks table
```sql
CREATE TABLE tasks (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    title VARCHAR(255) NOT NULL,
    description TEXT,
    completed BOOLEAN DEFAULT FALSE,
    user_id UUID REFERENCES users(id) ON DELETE CASCADE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

CREATE INDEX idx_tasks_user_id ON tasks(user_id);
CREATE INDEX idx_tasks_completed ON tasks(completed);
```

## Relationships

- **User → Task**: One-to-many relationship
  - A user can have multiple tasks
  - When a user is deleted, all their tasks are automatically deleted (CASCADE)
  - Foreign key constraint ensures referential integrity

## Constraints

- **Data Integrity**:
  - All foreign key relationships are enforced
  - Unique constraints on email and username in users table
  - Non-null constraints on required fields

- **Security**:
  - Passwords are stored as hashed values (never plain text)
  - User ID verification required for all task operations
  - JWT tokens must be valid and unexpired for access

## Indexes

- **users**:
  - Email index for efficient login lookups
  - Username index for efficient profile lookups

- **tasks**:
  - User ID index for efficient task filtering by user
  - Completed index for efficient status-based queries