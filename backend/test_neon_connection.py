import asyncio
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from backend.database import engine

async def test_connection():
    try:
        # Attempt to connect to the database
        with engine.connect() as conn:
            result = conn.execute("SELECT 1")
            print("Connection successful!")
            print(f"Result: {result.fetchone()}")
            return True
    except Exception as e:
        print(f"Connection failed: {e}")
        return False

if __name__ == "__main__":
    print("Testing connection to Neon database...")
    success = asyncio.run(test_connection())
    
    if success:
        print("\nThe backend is successfully connected to Neon server.")
    else:
        print("\nThe backend is NOT connected to Neon server or there's an issue with the connection.")