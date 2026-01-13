# API Contracts: General Update Feature

**Feature**: 001-update-feature
**Date**: 2026-01-13

## Overview

This document defines the API contracts for the update functionality of the Hackathon Todo Application. These contracts ensure compatibility with the existing Next.js frontend while implementing the required update features.

## Update Management Endpoints

### 1. Get Available Updates
- **Endpoint**: `GET /api/updates`
- **Description**: Retrieve a list of available updates
- **Authentication**: JWT required
- **Request Headers**:
  - Authorization: Bearer {jwt_token}
- **Response Codes**:
  - 200: Success - Returns list of available updates
  - 401: Unauthorized - Invalid or missing JWT token
  - 500: Server Error - Internal server error
- **Response Schema**:
  ```json
  [
    {
      "id": 1,
      "title": "string",
      "description": "string",
      "status": "pending|in-progress|completed|failed",
      "version": "string",
      "created_at": "datetime",
      "updated_at": "datetime",
      "applied_at": "datetime|null",
      "rollback_possible": "boolean"
    }
  ]
  ```

### 2. Get Update Details
- **Endpoint**: `GET /api/updates/{id}`
- **Description**: Retrieve details of a specific update
- **Authentication**: JWT required
- **Request Headers**:
  - Authorization: Bearer {jwt_token}
- **Parameters**:
  - id: Integer (Update ID)
- **Response Codes**:
  - 200: Success - Returns update details
  - 401: Unauthorized - Invalid or missing JWT token
  - 404: Not Found - Update with given ID not found
  - 500: Server Error - Internal server error
- **Response Schema**:
  ```json
  {
    "id": 1,
    "title": "string",
    "description": "string",
    "status": "pending|in-progress|completed|failed",
    "version": "string",
    "created_at": "datetime",
    "updated_at": "datetime",
    "applied_at": "datetime|null",
    "rollback_possible": "boolean"
  }
  ```

### 3. Apply an Update
- **Endpoint**: `POST /api/updates/{id}/apply`
- **Description**: Apply a specific update
- **Authentication**: JWT required
- **Request Headers**:
  - Authorization: Bearer {jwt_token}
- **Parameters**:
  - id: Integer (Update ID)
- **Response Codes**:
  - 200: Success - Update applied successfully
  - 401: Unauthorized - Invalid or missing JWT token
  - 404: Not Found - Update with given ID not found
  - 409: Conflict - Update cannot be applied due to current status
  - 500: Server Error - Internal server error
- **Response Schema**:
  ```json
  {
    "message": "string",
    "status": "completed|failed",
    "applied_at": "datetime"
  }
  ```

### 4. Rollback an Update
- **Endpoint**: `POST /api/updates/{id}/rollback`
- **Description**: Rollback a specific update
- **Authentication**: JWT required
- **Request Headers**:
  - Authorization: Bearer {jwt_token}
- **Parameters**:
  - id: Integer (Update ID)
- **Response Codes**:
  - 200: Success - Update rolled back successfully
  - 401: Unauthorized - Invalid or missing JWT token
  - 404: Not Found - Update with given ID not found
  - 409: Conflict - Update cannot be rolled back
  - 500: Server Error - Internal server error
- **Response Schema**:
  ```json
  {
    "message": "string",
    "status": "completed|failed",
    "rolled_back_at": "datetime"
  }
  ```

## Update Logging Endpoints

### 5. Get Update Logs
- **Endpoint**: `GET /api/updates/{update_id}/logs`
- **Description**: Retrieve logs for a specific update
- **Authentication**: JWT required
- **Request Headers**:
  - Authorization: Bearer {jwt_token}
- **Parameters**:
  - update_id: Integer (Update ID)
- **Query Parameters**:
  - level: Optional (Filter by log level: info, warning, error, critical)
  - limit: Optional (Number of logs to return, default: 50)
  - offset: Optional (Offset for pagination, default: 0)
- **Response Codes**:
  - 200: Success - Returns list of logs
  - 401: Unauthorized - Invalid or missing JWT token
  - 404: Not Found - Update with given ID not found
  - 500: Server Error - Internal server error
- **Response Schema**:
  ```json
  {
    "logs": [
      {
        "id": 1,
        "timestamp": "datetime",
        "level": "info|warning|error|critical",
        "message": "string",
        "component": "string|null"
      }
    ],
    "total_count": "integer",
    "limit": "integer",
    "offset": "integer"
  }
  ```

## Existing Task Management Endpoints (Maintained for Compatibility)

### 6. List User Tasks (Maintained)
- **Endpoint**: `GET /api/{user_id}/tasks`
- **Description**: List all tasks for a user (maintained for backward compatibility)
- **Authentication**: JWT required
- **Request Headers**:
  - Authorization: Bearer {jwt_token}
- **Parameters**:
  - user_id: Integer (User ID from JWT token must match)
- **Response Codes**:
  - 200: Success - Returns list of user's tasks
  - 401: Unauthorized - Invalid or missing JWT token
  - 403: Forbidden - User ID mismatch
  - 500: Server Error - Internal server error
- **Response Schema**:
  ```json
  [
    {
      "id": 1,
      "title": "string",
      "description": "string",
      "completed": "boolean",
      "user_id": "integer",
      "created_at": "datetime",
      "updated_at": "datetime"
    }
  ]
  ```

### 7. Create Task (Maintained)
- **Endpoint**: `POST /api/{user_id}/tasks`
- **Description**: Create a new task for a user (maintained for backward compatibility)
- **Authentication**: JWT required
- **Request Headers**:
  - Authorization: Bearer {jwt_token}
- **Parameters**:
  - user_id: Integer (User ID from JWT token must match)
- **Request Body**:
  ```json
  {
    "title": "string",
    "description": "string"
  }
  ```
- **Response Codes**:
  - 201: Created - Task created successfully
  - 400: Bad Request - Invalid request body
  - 401: Unauthorized - Invalid or missing JWT token
  - 403: Forbidden - User ID mismatch
  - 500: Server Error - Internal server error
- **Response Schema**:
  ```json
  {
    "id": 1,
    "title": "string",
    "description": "string",
    "completed": "boolean",
    "user_id": "integer",
    "created_at": "datetime",
    "updated_at": "datetime"
  }
  ```

### 8. Get Task Details (Maintained)
- **Endpoint**: `GET /api/{user_id}/tasks/{id}`
- **Description**: Get a single task's details (maintained for backward compatibility)
- **Authentication**: JWT required
- **Request Headers**:
  - Authorization: Bearer {jwt_token}
- **Parameters**:
  - user_id: Integer (User ID from JWT token must match)
  - id: Integer (Task ID)
- **Response Codes**:
  - 200: Success - Returns task details
  - 401: Unauthorized - Invalid or missing JWT token
  - 403: Forbidden - User ID mismatch
  - 404: Not Found - Task with given ID not found
  - 500: Server Error - Internal server error
- **Response Schema**:
  ```json
  {
    "id": 1,
    "title": "string",
    "description": "string",
    "completed": "boolean",
    "user_id": "integer",
    "created_at": "datetime",
    "updated_at": "datetime"
  }
  ```

### 9. Update Task (Maintained)
- **Endpoint**: `PUT /api/{user_id}/tasks/{id}`
- **Description**: Update a task's title/description (maintained for backward compatibility)
- **Authentication**: JWT required
- **Request Headers**:
  - Authorization: Bearer {jwt_token}
- **Parameters**:
  - user_id: Integer (User ID from JWT token must match)
  - id: Integer (Task ID)
- **Request Body**:
  ```json
  {
    "title": "string",
    "description": "string"
  }
  ```
- **Response Codes**:
  - 200: Success - Task updated successfully
  - 400: Bad Request - Invalid request body
  - 401: Unauthorized - Invalid or missing JWT token
  - 403: Forbidden - User ID mismatch
  - 404: Not Found - Task with given ID not found
  - 500: Server Error - Internal server error
- **Response Schema**:
  ```json
  {
    "id": 1,
    "title": "string",
    "description": "string",
    "completed": "boolean",
    "user_id": "integer",
    "created_at": "datetime",
    "updated_at": "datetime"
  }
  ```

### 10. Delete Task (Maintained)
- **Endpoint**: `DELETE /api/{user_id}/tasks/{id}`
- **Description**: Delete a task (maintained for backward compatibility)
- **Authentication**: JWT required
- **Request Headers**:
  - Authorization: Bearer {jwt_token}
- **Parameters**:
  - user_id: Integer (User ID from JWT token must match)
  - id: Integer (Task ID)
- **Response Codes**:
  - 204: No Content - Task deleted successfully
  - 401: Unauthorized - Invalid or missing JWT token
  - 403: Forbidden - User ID mismatch
  - 404: Not Found - Task with given ID not found
  - 500: Server Error - Internal server error
- **Response Schema**: Empty response body

### 11. Toggle Task Completion (Maintained)
- **Endpoint**: `PATCH /api/{user_id}/tasks/{id}/complete`
- **Description**: Toggle a task's completion status (maintained for backward compatibility)
- **Authentication**: JWT required
- **Request Headers**:
  - Authorization: Bearer {jwt_token}
- **Parameters**:
  - user_id: Integer (User ID from JWT token must match)
  - id: Integer (Task ID)
- **Response Codes**:
  - 200: Success - Task completion status toggled
  - 401: Unauthorized - Invalid or missing JWT token
  - 403: Forbidden - User ID mismatch
  - 404: Not Found - Task with given ID not found
  - 500: Server Error - Internal server error
- **Response Schema**:
  ```json
  {
    "id": 1,
    "title": "string",
    "description": "string",
    "completed": "boolean",
    "user_id": "integer",
    "created_at": "datetime",
    "updated_at": "datetime"
  }
  ```