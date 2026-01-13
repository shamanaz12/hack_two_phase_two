# API Contract: JWT Authentication

## Authentication Endpoints

### POST /api/auth/login
**Description**: Authenticate user and return JWT token
**Request**:
- Headers: Content-Type: application/json
- Body:
  ```json
  {
    "email": "string (required)",
    "password": "string (required)"
  }
  ```

**Response**:
- 200: OK
  ```json
  {
    "access_token": "string (JWT token)",
    "token_type": "string (bearer)"
  }
  ```
- 401: Unauthorized (Invalid credentials)

### POST /api/auth/register
**Description**: Register a new user
**Request**:
- Headers: Content-Type: application/json
- Body:
  ```json
  {
    "email": "string (required)",
    "username": "string (required)",
    "password": "string (required)"
  }
  ```

**Response**:
- 201: Created
  ```json
  {
    "id": "UUID",
    "email": "string",
    "username": "string"
  }
  ```
- 400: Bad Request (Validation error or duplicate user)

## Protected Task Endpoints (Require Authorization header)

### GET /api/{user_id}/tasks
**Description**: Get all tasks for the authenticated user
**Headers**: 
- Authorization: Bearer {token}
**Parameters**:
- user_id: UUID (must match authenticated user's ID)

**Response**:
- 200: OK
  ```json
  [
    {
      "id": "UUID",
      "title": "string",
      "description": "string (optional)",
      "completed": "boolean",
      "user_id": "UUID",
      "created_at": "datetime",
      "updated_at": "datetime"
    }
  ]
  ```
- 401: Unauthorized (Invalid or missing token)
- 403: Forbidden (user_id doesn't match token's user)

### POST /api/{user_id}/tasks
**Description**: Create a new task for the authenticated user
**Headers**: 
- Authorization: Bearer {token}
**Parameters**:
- user_id: UUID (must match authenticated user's ID)
**Request Body**:
  ```json
  {
    "title": "string (required)",
    "description": "string (optional)"
  }
  ```

**Response**:
- 201: Created
  ```json
  {
    "id": "UUID",
    "title": "string",
    "description": "string (optional)",
    "completed": "boolean",
    "user_id": "UUID",
    "created_at": "datetime",
    "updated_at": "datetime"
  }
  ```
- 401: Unauthorized
- 403: Forbidden

### GET /api/{user_id}/tasks/{id}
**Description**: Get a specific task for the authenticated user
**Headers**: 
- Authorization: Bearer {token}
**Parameters**:
- user_id: UUID (must match authenticated user's ID)
- id: UUID (task ID)

**Response**:
- 200: OK
  ```json
  {
    "id": "UUID",
    "title": "string",
    "description": "string (optional)",
    "completed": "boolean",
    "user_id": "UUID",
    "created_at": "datetime",
    "updated_at": "datetime"
  }
  ```
- 401: Unauthorized
- 403: Forbidden
- 404: Not Found

### PUT /api/{user_id}/tasks/{id}
**Description**: Update a specific task for the authenticated user
**Headers**: 
- Authorization: Bearer {token}
**Parameters**:
- user_id: UUID (must match authenticated user's ID)
- id: UUID (task ID)
**Request Body**:
  ```json
  {
    "title": "string (optional)",
    "description": "string (optional)",
    "completed": "boolean (optional)"
  }
  ```

**Response**:
- 200: OK
  ```json
  {
    "id": "UUID",
    "title": "string",
    "description": "string (optional)",
    "completed": "boolean",
    "user_id": "UUID",
    "created_at": "datetime",
    "updated_at": "datetime"
  }
  ```
- 401: Unauthorized
- 403: Forbidden
- 404: Not Found

### DELETE /api/{user_id}/tasks/{id}
**Description**: Delete a specific task for the authenticated user
**Headers**: 
- Authorization: Bearer {token}
**Parameters**:
- user_id: UUID (must match authenticated user's ID)
- id: UUID (task ID)

**Response**:
- 204: No Content
- 401: Unauthorized
- 403: Forbidden
- 404: Not Found

### PATCH /api/{user_id}/tasks/{id}/complete
**Description**: Toggle completion status of a specific task for the authenticated user
**Headers**: 
- Authorization: Bearer {token}
**Parameters**:
- user_id: UUID (must match authenticated user's ID)
- id: UUID (task ID)

**Response**:
- 200: OK
  ```json
  {
    "id": "UUID",
    "title": "string",
    "description": "string (optional)",
    "completed": "boolean",
    "user_id": "UUID",
    "created_at": "datetime",
    "updated_at": "datetime"
  }
  ```
- 401: Unauthorized
- 403: Forbidden
- 404: Not Found