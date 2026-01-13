from contextlib import asynccontextmanager
from fastapi import FastAPI
from backend.database import engine
from backend.models import SQLModel, User, Task, Update, UpdateLog
from typing import AsyncGenerator


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    """
    Lifespan event handler to create database tables on startup
    """
    # Startup event: Create all database tables in the correct order
    print("Creating database tables...")

    # Create tables in dependency order (User first, since Task depends on it)
    with engine.connect() as conn:
        # Create tables in the right order to satisfy foreign key constraints
        User.metadata.create_all(bind=engine)
        Update.metadata.create_all(bind=engine)
        Task.metadata.create_all(bind=engine)
        UpdateLog.metadata.create_all(bind=engine)

    print("Database tables created successfully!")

    yield  # Application runs during this period

    # Shutdown event: Cleanup can be done here if needed
    print("Shutting down...")