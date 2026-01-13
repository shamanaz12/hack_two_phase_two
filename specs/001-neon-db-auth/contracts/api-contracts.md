# API Contracts: Todo Application Backend

**Feature**: Neon PostgreSQL Database & Better Auth Integration
**Date**: 2026-01-12
**Author**: Qwen - The Cloud Database Wizard & Infrastructure Sorcerer

## Overview

This document defines the API contracts for the Todo application backend, ensuring compatibility with the existing Next.js frontend and following RESTful principles.

## Authentication

All endpoints (except authentication endpoints) require a valid JWT token in the Authorization header:

```
Authorization: Bearer <jwt_token>
```

The JWT token must contain a `user_id` claim that matches the `user_id` in the endpoint path for authorization validation.

## Base URL

```
http://localhost:8000/api
```

## Endpoints

### 1. List all tasks for a user

- **Endpoint**: `GET /{user_id}/tasks`
- **Description**: Retrieve all tasks for a specific user
- **Authentication**: Required
- **Path Parameters**:
  - `user_id` (string, required): The ID of the user whose tasks to retrieve
- **Headers**:
  - `Authorization` (string, required): Bearer token
- **Response**:
  - `200 OK`: Successfully retrieved tasks
    - Content-Type: `application/json`
    - Body: Array of Task objects

#### Request Example
```
GET /123e4567-e89b-12d3-a456-426614174000/tasks
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

#### Response Example
```json
[
  {
    "id": "123e4567-e89b-12d3-a456-426614174001",
    "title": "Sample Task",
    "description": "This is a sample task",
    "completed": false,
    "user_id": "123e4567-e89b-12d3-a456-426614174000",
    "created_at": "2023-01-01T00:00:00Z",
    "updated_at": "2023-01-01T00:00:00Z"
  }
]
```

### 2. Create a new task for a user

- **Endpoint**: `POST /{user_id}/tasks`
- **Description**: Create a new task for a specific user
- **Authentication**: Required
- **Path Parameters**:
  - `user_id` (string, required): The ID of the user creating the task
- **Headers**:
  - `Authorization` (string, required): Bearer token
  - `Content-Type` (string, required): application/json
- **Request Body**:
  - `title` (string, required): The title of the task
  - `description` (string, optional): The description of the task
- **Response**:
  - `201 Created`: Task successfully created
    - Content-Type: `application/json`
    - Body: Created Task object
  - `400 Bad Request`: Invalid input data
  - `401 Unauthorized`: Invalid or missing token
  - `403 Forbidden`: User ID mismatch or insufficient permissions

#### Request Example
```json
POST /123e4567-e89b-12d3-a456-426614174000/tasks
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
Content-Type: application/json

{
  "title": "New Task",
  "description": "This is a new task"
}
```

#### Response Example
```json
{
  "id": "123e4567-e89b-12d3-a456-426614174002",
  "title": "New Task",
  "description": "This is a new task",
  "completed": false,
  "user_id": "123e4567-e89b-12d3-a456-426614174000",
  "created_at": "2023-01-01T00:00:00Z",
  "updated_at": "2023-01-01T00:00:00Z"
}
```

### 3. Get a single task's details

- **Endpoint**: `GET /{user_id}/tasks/{task_id}`
- **Description**: Retrieve details of a specific task
- **Authentication**: Required
- **Path Parameters**:
  - `user_id` (string, required): The ID of the user who owns the task
  - `task_id` (string, required): The ID of the task to retrieve
- **Headers**:
  - `Authorization` (string, required): Bearer token
- **Response**:
  - `200 OK`: Successfully retrieved task
    - Content-Type: `application/json`
    - Body: Task object
  - `401 Unauthorized`: Invalid or missing token
  - `403 Forbidden`: User ID mismatch or insufficient permissions
  - `404 Not Found`: Task not found

#### Request Example
```
GET /123e4567-e89b-12d3-a456-426614174000/tasks/123e4567-e89b-12d3-a456-426614174002
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

#### Response Example
```json
{
  "id": "123e4567-e89b-12d3-a456-426614174002",
  "title": "New Task",
  "description": "This is a new task",
  "completed": false,
  "user_id": "123e4567-e89b-12d3-a456-426614174000",
  "created_at": "2023-01-01T00:00:00Z",
  "updated_at": "2023-01-01T00:00:00Z"
}
```

### 4. Update a task's title/description

- **Endpoint**: `PUT /{user_id}/tasks/{task_id}`
- **Description**: Update a task's title and/or description
- **Authentication**: Required
- **Path Parameters**:
  - `user_id` (string, required): The ID of the user who owns the task
  - `task_id` (string, required): The ID of the task to update
- **Headers**:
  - `Authorization` (string, required): Bearer token
  - `Content-Type` (string, required): application/json
- **Request Body**:
  - `title` (string, optional): The new title of the task
  - `description` (string, optional): The new description of the task
  - `completed` (boolean, optional): The new completion status
- **Response**:
  - `200 OK`: Task successfully updated
    - Content-Type: `application/json`
    - Body: Updated Task object
  - `400 Bad Request`: Invalid input data
  - `401 Unauthorized`: Invalid or missing token
  - `403 Forbidden`: User ID mismatch or insufficient permissions
  - `404 Not Found`: Task not found

#### Request Example
```json
PUT /123e4567-e89b-12d3-a456-426614174000/tasks/123e4567-e89b-12d3-a456-426614174002
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
Content-Type: application/json

{
  "title": "Updated Task",
  "description": "This is an updated task"
}
```

#### Response Example
```json
{
  "id": "123e4567-e89b-12d3-a456-426614174002",
  "title": "Updated Task",
  "description": "This is an updated task",
  "completed": false,
  "user_id": "123e4567-e89b-12d3-a456-426614174000",
  "created_at": "2023-01-01T00:00:00Z",
  "updated_at": "2023-01-01T00:00:01Z"
}
```

### 5. Delete a task

- **Endpoint**: `DELETE /{user_id}/tasks/{task_id}`
- **Description**: Delete a specific task
- **Authentication**: Required
- **Path Parameters**:
  - `user_id` (string, required): The ID of the user who owns the task
  - `task_id` (string, required): The ID of the task to delete
- **Headers**:
  - `Authorization` (string, required): Bearer token
- **Response**:
  - `204 No Content`: Task successfully deleted
  - `401 Unauthorized`: Invalid or missing token
  - `403 Forbidden`: User ID mismatch or insufficient permissions
  - `404 Not Found`: Task not found

#### Request Example
```
DELETE /123e4567-e89b-12d3-a456-426614174000/tasks/123e4567-e89b-12d3-a456-426614174002
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

#### Response Example
```
Status: 204 No Content
```

### 6. Toggle a task's completion status

- **Endpoint**: `PATCH /{user_id}/tasks/{task_id}/complete`
- **Description**: Toggle a task's completion status
- **Authentication**: Required
- **Path Parameters**:
  - `user_id` (string, required): The ID of the user who owns the task
  - `task_id` (string, required): The ID of the task to update
- **Headers**:
  - `Authorization` (string, required): Bearer token
- **Response**:
  - `200 OK`: Task completion status successfully toggled
    - Content-Type: `application/json`
    - Body: Updated Task object
  - `401 Unauthorized`: Invalid or missing token
  - `403 Forbidden`: User ID mismatch or insufficient permissions
  - `404 Not Found`: Task not found

#### Request Example
```
PATCH /123e4567-e89b-12d3-a456-426614174000/tasks/123e4567-e89b-12d3-a456-426614174002/complete
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

#### Response Example
```json
{
  "id": "123e4567-e89b-12d3-a456-426614174002",
  "title": "Updated Task",
  "description": "This is an updated task",
  "completed": true,
  "user_id": "123e4567-e89b-12d3-a456-426614174000",
  "created_at": "2023-01-01T00:00:00Z",
  "updated_at": "2023-01-01T00:00:02Z"
}
```

## Error Responses

All error responses follow this structure:

```json
{
  "detail": "Error message describing the issue"
}
```

## Common HTTP Status Codes

- `200 OK`: Request successful
- `201 Created`: Resource successfully created
- `204 No Content`: Request successful, no content to return
- `400 Bad Request`: Invalid request parameters or body
- `401 Unauthorized`: Missing or invalid authentication token
- `403 Forbidden`: Insufficient permissions or user ID mismatch
- `404 Not Found`: Requested resource does not exist
- `500 Internal Server Error`: Unexpected server error