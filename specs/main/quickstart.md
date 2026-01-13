# Quickstart Guide: JWT Authentication Implementation

## Setting Up JWT Authentication

### 1. Environment Configuration
Set up the required environment variables:

```bash
# In your .env file
BETTER_AUTH_SECRET=your-super-secret-key-change-in-production
DATABASE_URL=postgresql://username:password@ep-aged-math-123456.us-east-1.aws.neon.tech/neondb?sslmode=require
```

### 2. Frontend Configuration (Next.js)
1. Configure Better Auth with JWT plugin in your frontend:
   ```javascript
   // lib/auth.ts (or similar)
   import { betterAuth } from "better-auth";
   
   export const auth = betterAuth({
     secret: process.env.BETTER_AUTH_SECRET,
     // other configurations
   });
   ```

2. Update your API client to automatically attach JWT tokens:
   ```typescript
   // lib/api.ts
   import axios from 'axios';
   
   const apiClient = axios.create({
     baseURL: process.env.NEXT_PUBLIC_API_BASE_URL || 'http://localhost:8000',
   });
   
   // Interceptor to add JWT token to requests
   apiClient.interceptors.request.use((config) => {
     const token = localStorage.getItem('jwt_token'); // or however you store the token
     if (token) {
       config.headers.Authorization = `Bearer ${token}`;
     }
     return config;
   });
   
   export default apiClient;
   ```

### 3. Backend Configuration (FastAPI)
1. Create the JWT verification dependency:
   ```python
   # backend/dependencies.py
   from fastapi import Depends, HTTPException, status
   from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
   import jwt
   import os
   
   security = HTTPBearer()
   
   def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)):
       try:
           token = credentials.credentials
           payload = jwt.decode(token, os.getenv("BETTER_AUTH_SECRET"), algorithms=["HS256"])
           user_id: str = payload.get("sub")
           if user_id is None:
               raise HTTPException(status_code=401, detail="Invalid token")
           return {"user_id": user_id}
       except jwt.ExpiredSignatureError:
           raise HTTPException(status_code=401, detail="Token has expired")
       except jwt.JWTError:
           raise HTTPException(status_code=401, detail="Invalid token")
   ```

2. Apply the dependency to all task endpoints:
   ```python
   # backend/routes/tasks.py
   @router.post("/tasks", ...)
   async def create_task(user_id: str, ..., current_user: dict = Depends(get_current_user)):
       # Verify that the user_id in the URL matches the user_id in the token
       if user_id != current_user["user_id"]:
           raise HTTPException(status_code=403, detail="Access denied")
       
       # Add user_id to the task creation
       db_task = Task(title=..., user_id=current_user["user_id"])
       ...
   ```

### 4. Testing the Authentication
1. Register a new user via the registration endpoint
2. Log in to obtain a JWT token
3. Use the token in the Authorization header for subsequent requests
4. Verify that users can only access their own tasks

### 5. Data Isolation Verification
Ensure that all database queries are scoped to the authenticated user:
- When getting tasks: `SELECT * FROM tasks WHERE user_id = current_user_id`
- When updating/deleting: Verify the task belongs to the current user before performing the operation