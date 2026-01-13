import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.routes import tasks, updates
from backend.lifespan import lifespan
from backend.exception_handlers import add_exception_handlers

app = FastAPI(
    title="Todo App with Update Management API",
    description="API for managing todos with update capabilities",
    version="1.0.0",
    # lifespan=lifespan  # Temporarily commented out to bypass table creation issue
)

# Add CORS middleware to allow communication with frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Add exception handlers for safe error messages
add_exception_handlers(app)

# Include routers
app.include_router(tasks.router, prefix="/api/{user_id}", tags=["tasks"])
app.include_router(updates.router, prefix="/api", tags=["updates"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the Todo App with Update Management API"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}