"""Test script to verify Neon database connection and perform basic operations"""

import asyncio
import uuid
from datetime import datetime
from backend.database import AsyncSessionLocal
from backend.models import Task


async def test_connection():
    """Test the database connection by inserting and retrieving a task"""
    print("Testing database connection...")
    
    async with AsyncSessionLocal() as session:
        # Create a test task
        test_task = Task(
            title="Test Task",
            description="This is a test task created to verify the database connection",
            completed=False,
            user_id=uuid.uuid4()  # Generate a random user ID for testing
        )
        
        # Add the task to the session
        session.add(test_task)
        
        # Commit the transaction
        await session.commit()
        
        # Refresh to get the auto-generated fields
        await session.refresh(test_task)
        
        print(f"Task created successfully with ID: {test_task.id}")
        
        # Retrieve the task to verify it was stored
        retrieved_task = await session.get(Task, test_task.id)
        
        if retrieved_task:
            print(f"Task retrieved successfully: {retrieved_task.title}")
            print(f"Description: {retrieved_task.description}")
            print(f"Completed: {retrieved_task.completed}")
            print(f"User ID: {retrieved_task.user_id}")
        else:
            print("Failed to retrieve the task")
    
    print("Database connection test completed successfully!")


if __name__ == "__main__":
    asyncio.run(test_connection())