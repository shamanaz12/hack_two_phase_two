# Todo App with Update Management

This is a full-stack application for a todo management system with update management capabilities. It includes both a Next.js 14.2.5 frontend and a Python FastAPI backend with update functionality.

## Features

- User authentication (login/signup)
- Dashboard showing user's task list
- Create, read, update, and delete tasks
- Inline task editing with save/cancel functionality
- Toggle task completion status
- Update management system with rollback capabilities
- Comprehensive logging for audit and troubleshooting
- Responsive design with Tailwind CSS

## Architecture

- **Frontend**: Next.js 14.2.5 with App Router, TypeScript, Tailwind CSS, Better Auth
- **Backend**: Python FastAPI with SQLModel, Pydantic, JWT Authentication
- **Database**: Neon PostgreSQL
- **Update System**: Managed updates with rollback and logging capabilities

## Tech Stack

- Next.js 14.2.5 with App Router
- React 18.2.0
- TypeScript
- Tailwind CSS
- Better Auth for authentication
- Python 3.11+
- FastAPI for backend API
- SQLModel for database modeling
- Pydantic for data validation
- JWT for authentication
- Neon PostgreSQL for database
- Axios for API requests

## Getting Started

### Backend Setup

1. Navigate to the backend directory:
   ```bash
   cd backend
   ```

2. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up environment variables by creating a `.env` file:
   ```bash
   DATABASE_URL=postgresql://username:password@localhost:5432/todo_app
   NEON_DATABASE_URL=your_neon_postgres_connection_string
   JWT_SECRET_KEY=your-super-secret-jwt-key-change-in-production
   ```

4. Start the backend server:
   ```bash
   uvicorn main:app --reload
   ```

### Frontend Setup

1. Install dependencies:
   ```bash
   npm install
   ```

2. Set up environment variables by copying `.env.example` to `.env.local` and updating the values:
   ```bash
   NEXT_PUBLIC_API_BASE_URL=http://localhost:8000
   NEXT_PUBLIC_BASE_URL=http://localhost:3000
   ```

3. Run the development server:
   ```bash
   npm run dev
   ```

4. Open [http://localhost:3000](http://localhost:3000) in your browser to see the application.

## Project Structure

### Backend
```
backend/
├── main.py                 # FastAPI application entry point
├── models.py               # SQLModel models (Task, Update, UpdateLog)
├── database.py             # Database connection
├── dependencies.py         # JWT authentication
├── routes/                 # API routes
│   ├── tasks.py            # Task management endpoints
│   └── updates.py          # Update management endpoints
├── services/               # Business logic
│   └── update_service.py   # Update operations
├── backend_logging.py      # Logging infrastructure
├── requirements.txt        # Python dependencies
└── .env                    # Environment variables
```

### Frontend
```
app/                    # Next.js App Router pages
├── layout.tsx          # Root layout
├── page.tsx            # Dashboard page
├── login/              # Login page
├── signup/             # Signup page
└── tasks/[id]/         # Task detail page
components/             # Reusable React components
├── Header.tsx          # Navigation header
├── TaskList.tsx        # Task list component
├── TaskItem.tsx        # Individual task component
└── TaskForm.tsx        # Task creation form
lib/                    # Utility functions and API clients
├── api.ts              # API service layer
└── auth.ts             # Authentication client
types/                  # TypeScript type definitions
├── index.ts            # User and Task interfaces
```

## API Integration

The application connects to a backend API at the endpoints specified in the API contract:

### Task Management
- GET/POST `/api/{user_id}/tasks`
- GET/PUT/DELETE `/api/{user_id}/tasks/{id}`
- PATCH `/api/{user_id}/tasks/{id}/complete`

### Update Management
- GET `/api/updates` - List all available updates
- GET `/api/updates/{id}` - Get specific update details
- POST `/api/updates/{id}/apply` - Apply an update
- POST `/api/updates/{id}/rollback` - Rollback an update
- GET `/api/updates/{update_id}/logs` - Get update logs

All API calls include proper error handling and loading states.

## Update Management System

The backend includes a comprehensive update management system that allows for:
- Applying updates to the system
- Rolling back updates if needed
- Comprehensive logging for audit and troubleshooting
- Preserving 95% backward compatibility during updates
- Maintaining zero data loss during updates

## Authentication

Authentication is handled using Better Auth for the frontend and JWT tokens for backend API communication. The application redirects unauthenticated users to the login page when accessing protected routes.