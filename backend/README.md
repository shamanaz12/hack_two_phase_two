# Todo App Backend

This is the backend for the Todo application, built with FastAPI and SQLModel. It provides a secure API for managing user tasks with JWT authentication and Neon PostgreSQL database.

## Features

- Secure JWT-based authentication
- Full CRUD operations for tasks
- Task completion toggling
- User-specific task isolation
- Async database operations with Neon PostgreSQL

## API Endpoints

The backend implements the following 6 required endpoints:

- `GET    /api/{user_id}/tasks` - Retrieve all tasks for a user
- `POST   /api/{user_id}/tasks` - Create a new task for a user
- `GET    /api/{user_id}/tasks/{id}` - Retrieve a specific task
- `PUT    /api/{user_id}/tasks/{id}` - Update a specific task
- `DELETE /api/{user_id}/tasks/{id}` - Delete a specific task
- `PATCH  /api/{user_id}/tasks/{id}/complete` - Toggle task completion status

## Project Structure

```
/backend
├── main.py                 # FastAPI application entry point
├── models.py               # SQLModel Task model
├── database.py             # Neon DB connection
├── dependencies.py         # JWT Auth dependency
├── routes/                 # API routes
│   └── tasks.py            # All 6 endpoints
├── init_db.py              # Database initialization script
├── test_connection.py      # Connection test script
├── .env                    # Environment variables
└── requirements.txt        # Project dependencies
```

## Neon Database Setup

### Phase A: Neon Portal Setup

1. Go to [Neon Console](https://console.neon.tech/) and create an account
2. Create a new project (e.g., "todo-app")
3. Copy the connection string from the project dashboard
4. The connection string will look like: `postgresql://username:password@ep-aged-math-123456.us-east-1.aws.neon.tech/neondb`

### Phase B: Local Environment Configuration

1. Create a `.env` file in the backend directory with your Neon connection string:
   ```bash
   DATABASE_URL=postgresql://username:password@ep-aged-math-123456.us-east-1.aws.neon.tech/neondb
   SECRET_KEY=your-super-secret-key-change-in-production
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Phase C: Schema Creation & Verification

1. Initialize the database tables:
   ```bash
   python init_db.py
   ```

2. Test the connection:
   ```bash
   python test_connection.py
   ```

## Running with Uvicorn

To run the application in development mode:

```bash
cd backend
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`.

## Environment Variables

- `DATABASE_URL`: Connection string for the Neon PostgreSQL database (stored in `.env`)
- `SECRET_KEY`: Secret key for JWT token signing (change in production!)

## Authentication

All endpoints require a valid JWT token in the Authorization header:

```
Authorization: Bearer <token>
```

The token should contain the user ID in the payload to ensure proper access control.