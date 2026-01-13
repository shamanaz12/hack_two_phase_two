# Quickstart Guide: General Update Feature

**Feature**: 001-update-feature
**Date**: 2026-01-13

## Overview

This guide provides instructions for quickly getting started with the update functionality of the Hackathon Todo Application. It covers setup, configuration, and basic usage of the update system.

## Prerequisites

- Python 3.11+
- pip package manager
- Git
- Access to Neon PostgreSQL database
- Valid JWT token for authentication

## Setup Instructions

### 1. Clone the Repository

```bash
git clone <repository-url>
cd <repository-directory>
```

### 2. Set Up Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r backend/requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the backend directory with the following variables:

```bash
DATABASE_URL="postgresql://username:password@host:port/database_name"
JWT_SECRET_KEY="your-super-secret-jwt-key"
NEON_DATABASE_URL="your-neon-postgres-connection-string"
```

### 5. Run Database Migrations

```bash
cd backend
python -m alembic upgrade head
```

## Starting the Service

### 1. Navigate to Backend Directory

```bash
cd backend
```

### 2. Start the Server

```bash
uvicorn main:app --reload
```

The server will start on `http://localhost:8000` by default.

## Basic Usage

### 1. Authenticating with the API

All update endpoints require a valid JWT token. Obtain a token through the authentication endpoint:

```bash
POST /auth/token
Content-Type: application/json

{
  "username": "your_username",
  "password": "your_password"
}
```

### 2. Checking Available Updates

To see what updates are available:

```bash
curl -X GET \
  http://localhost:8000/api/updates \
  -H "Authorization: Bearer YOUR_JWT_TOKEN"
```

### 3. Applying an Update

To apply a specific update:

```bash
curl -X POST \
  http://localhost:8000/api/updates/1/apply \
  -H "Authorization: Bearer YOUR_JWT_TOKEN"
```

### 4. Viewing Update Logs

To see logs for a specific update:

```bash
curl -X GET \
  http://localhost:8000/api/updates/1/logs \
  -H "Authorization: Bearer YOUR_JWT_TOKEN"
```

### 5. Rolling Back an Update

To roll back a specific update:

```bash
curl -X POST \
  http://localhost:8000/api/updates/1/rollback \
  -H "Authorization: Bearer YOUR_JWT_TOKEN"
```

## Testing the System

### 1. Run Unit Tests

```bash
cd backend
python -m pytest tests/unit/
```

### 2. Run Integration Tests

```bash
cd backend
python -m pytest tests/integration/
```

### 3. Verify API Endpoints

Use the following commands to verify that all endpoints are working:

```bash
# Check if service is running
curl http://localhost:8000/health

# List available updates
curl -X GET http://localhost:8000/api/updates -H "Authorization: Bearer YOUR_JWT_TOKEN"

# Get specific update details
curl -X GET http://localhost:8000/api/updates/1 -H "Authorization: Bearer YOUR_JWT_TOKEN"
```

## Troubleshooting

### Common Issues

1. **Database Connection Error**
   - Verify that your Neon PostgreSQL credentials are correct
   - Check that the database URL is properly formatted

2. **JWT Authentication Failure**
   - Ensure your JWT token is valid and not expired
   - Verify that the secret key matches between frontend and backend

3. **Port Already in Use**
   - Change the port in your uvicorn command: `uvicorn main:app --reload --port 8001`

### Useful Commands

- Check server status: `curl http://localhost:8000/health`
- View application logs: `tail -f logs/app.log`
- Reset database: `python reset_db.py` (for development only)

## Next Steps

1. Review the API documentation for complete endpoint details
2. Implement proper error handling in your client application
3. Set up monitoring for update processes
4. Configure automated backup before applying updates