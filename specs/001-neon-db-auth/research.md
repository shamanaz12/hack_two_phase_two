# Research: Neon PostgreSQL Database & Better Auth Integration

**Feature**: Neon PostgreSQL Database & Better Auth Integration
**Date**: 2026-01-12
**Author**: Qwen - The Cloud Database Wizard & Infrastructure Sorcerer

## Research Objectives

This research addresses the technical requirements for setting up Neon PostgreSQL database and integrating Better Auth with JWT verification for the Todo application backend.

## Decision Log

### 1. Neon PostgreSQL Account Setup
- **Decision**: Use Neon's free tier for development and testing
- **Rationale**: Neon offers a generous free tier that's suitable for development and small-scale production applications. It provides serverless PostgreSQL with instant scaling.
- **Alternatives considered**: 
  - Self-hosted PostgreSQL: Requires more maintenance and setup
  - AWS RDS: More complex setup and higher costs for development
  - Supabase: Good alternative but Neon is specifically requested

### 2. Database Connection Security
- **Decision**: Use SSL connection with Neon PostgreSQL
- **Rationale**: Neon requires SSL connections for security. This ensures encrypted communication between the application and database.
- **Implementation**: Use `connect_args={"sslmode": "require"}` in the SQLModel engine configuration

### 3. Environment Variable Management
- **Decision**: Store database credentials in `.env` file using `python-dotenv`
- **Rationale**: This follows security best practices by keeping sensitive information out of source code
- **Implementation**: Create `.env` file in backend directory and load with `dotenv.load_dotenv()`

### 4. Better Auth Integration Approach
- **Decision**: Use Better Auth's JWT tokens for backend authentication
- **Rationale**: Better Auth provides a complete authentication solution that can issue JWT tokens, which can be verified by the backend
- **Implementation**: Extract JWT from Authorization header and verify using the same secret as Better Auth

### 5. User ID Verification Method
- **Decision**: Compare user_id from JWT token with user_id in API endpoint path
- **Rationale**: This ensures users can only access their own data by validating the token matches the requested resource
- **Implementation**: Create a dependency function that extracts and compares user IDs

## Technical Specifications

### Neon PostgreSQL Connection String Format
```
postgresql://username:password@ep-cool-cloud-123.us-east-1.aws.neon.tech/dbname
```

### Environment Variables Required
- `DATABASE_URL`: Connection string for Neon PostgreSQL
- `BETTER_AUTH_SECRET`: Shared secret for JWT verification

### SQLModel Engine Configuration
```python
engine = create_async_engine(
    DATABASE_URL,
    echo=True,
    pool_pre_ping=True,
    connect_args={"sslmode": "require"}
)
```

## Security Considerations

1. **Never commit credentials**: The `.env` file should be added to `.gitignore`
2. **Validate JWT tokens**: Always verify the token signature before processing requests
3. **Compare user IDs**: Ensure the user_id in the token matches the user_id in the endpoint
4. **Use HTTPS in production**: Ensure all communication is encrypted

## Implementation Steps Summary

1. Set up Neon PostgreSQL account and project
2. Create `.env` file with `DATABASE_URL`
3. Update `database.py` to use environment variable and SSL
4. Create JWT verification dependency in `dependencies.py`
5. Apply authentication to all task endpoints
6. Test connection and authentication flow