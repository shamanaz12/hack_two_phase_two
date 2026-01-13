# Research: JWT-Based Authentication Bridge

## Decision: JWT Token Flow Architecture
**Rationale**: The frontend (Better Auth) will issue JWT tokens upon successful authentication. These tokens will be stored client-side and attached to every API request to the backend. The backend will verify the JWT using the same shared secret and extract the user ID to scope database queries.

## Decision: Shared Secret Management
**Rationale**: A shared secret (BETTER_AUTH_SECRET) will be used by both frontend and backend to sign and verify JWT tokens. This secret will be stored in environment variables to ensure security.

## Decision: Token Attachment Method
**Rationale**: The frontend will intercept all API calls to the backend and automatically attach the JWT token in the Authorization header as "Authorization: Bearer <token>". This ensures transparent authentication without requiring manual token management in each API call.

## Decision: Backend Token Verification
**Rationale**: The backend will create a dependency function (get_current_user) that extracts the JWT from the Authorization header, verifies it using the shared secret, and returns the user information. This dependency will be applied to all protected endpoints.

## Decision: Data Isolation Implementation
**Rationale**: Each database query will be scoped to the authenticated user by including a WHERE clause that filters by the user ID extracted from the JWT token. This ensures that users can only access their own data.

## Alternatives Considered:
1. Session-based authentication - Rejected because it requires server-side state management and doesn't scale well with microservices
2. OAuth 2.0 with Bearer tokens - More complex than needed for this application
3. API keys per user - Less secure than properly implemented JWT with expiration