from setuptools import setup, find_packages

setup(
    name="todo-backend",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "fastapi==0.104.1",
        "sqlmodel==0.0.8",
        "pydantic==2.5.0",
        "pydantic-settings==2.1.0",
        "uvicorn[standard]==0.24.0",
        "psycopg2-binary==2.9.9",
        "python-jose[cryptography]==3.3.0",
        "passlib[bcrypt]==1.7.4",
        "python-multipart==0.0.6",
        "alembic==1.13.1",
        "sqlalchemy==2.0.23",
        "asyncpg==0.29.0",
        "pytest==7.4.3",
        "pytest-asyncio==0.21.1",
        "httpx==0.25.2",
    ],
    author="Todo App Team",
    author_email="team@todoapp.com",
    description="A todo app backend with update management",
    python_requires=">=3.7",
)