# Data Model: JWT Authentication System

## JWT Token Structure
- **Header**: Algorithm (HS256) and Token Type (JWT)
- **Payload**: 
  - `sub`: Subject (user ID)
  - `name`: User's name
  - `email`: User's email
  - `iat`: Issued at time
  - `exp`: Expiration time
- **Signature**: Generated using the shared secret

## User Entity
- **Fields**:
  - `id`: UUID (Primary Key)
  - `email`: String (Unique, Indexed)
  - `username`: String (Unique, Indexed)
  - `hashed_password`: String (For basic auth if needed)
  - `created_at`: DateTime
  - `updated_at`: DateTime
  - `is_active`: Boolean

## Task Entity (Updated)
- **Fields**:
  - `id`: UUID (Primary Key)
  - `title`: String
  - `description`: String (Optional)
  - `completed`: Boolean (Default: False)
  - `user_id`: UUID (Foreign Key to User)
  - `created_at`: DateTime
  - `updated_at`: DateTime

## Authentication Flow Data Requirements
- **Login Request**: email, password
- **Login Response**: JWT token
- **Token Validation**: Extract user_id from token payload
- **Database Scoping**: Use user_id to filter queries

## Validation Rules
- JWT tokens must be properly signed and not expired
- User IDs in tokens must correspond to valid users in the database
- All task operations must be scoped to the authenticated user