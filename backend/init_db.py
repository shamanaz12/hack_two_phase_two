"""Database initialization script for creating tables in Neon PostgreSQL"""

import asyncio
from sqlmodel import SQLModel
from backend.database import engine
from backend.models import Task


async def create_tables():
    """Create all tables in the database"""
    async with engine.begin() as conn:
        # Create tables
        await conn.run_sync(SQLModel.metadata.create_all)
    print("Tables created successfully!")


if __name__ == "__main__":
    asyncio.run(create_tables())