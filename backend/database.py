from sqlalchemy import create_engine
from sqlalchemy.pool import QueuePool
from sqlmodel import Session
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get database URL from environment variables
DATABASE_URL = os.getenv("DATABASE_URL", os.getenv("NEON_DATABASE_URL", "sqlite:///./todo_app.db"))

# Create the engine with connection pooling and SSL requirements
connect_args = {"sslmode": "require"} if "neon" in DATABASE_URL.lower() else {}
engine = create_engine(
    DATABASE_URL,
    poolclass=QueuePool,
    pool_size=5,
    max_overflow=10,
    pool_pre_ping=True,  # Required for reliable connections
    pool_recycle=300,
    echo=True,  # Enable SQL logging for debugging
    connect_args=connect_args  # Required for Neon SSL connections
)

def get_session():
    with Session(engine) as session:
        yield session