from datetime import datetime
from typing import Optional
from sqlmodel import SQLModel, Field, Relationship
from pydantic import BaseModel


# User model
class User(SQLModel, table=True):
    __tablename__ = "users"

    id: Optional[int] = Field(default=None, primary_key=True)
    username: str = Field(unique=True)
    email: str = Field(unique=True)
    hashed_password: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


# Request/Response models (Pydantic)
class UpdateBase(BaseModel):
    title: str
    description: Optional[str] = None
    version: str


class UpdateCreate(UpdateBase):
    pass


class UpdateRead(UpdateBase):
    id: int
    status: str
    created_at: datetime
    updated_at: datetime
    applied_at: Optional[datetime] = None
    rollback_possible: bool = True


class UpdateUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[str] = None


class UpdateApply(BaseModel):
    message: str
    status: str
    applied_at: Optional[datetime] = None


class UpdateRollback(BaseModel):
    message: str
    status: str
    rolled_back_at: Optional[datetime] = None


class UpdateLogBase(BaseModel):
    update_id: int
    level: str
    message: str
    component: Optional[str] = None


class UpdateLogCreate(UpdateLogBase):
    pass


class UpdateLogRead(UpdateLogBase):
    id: int
    timestamp: datetime


# Database models (SQLModel)
class Update(SQLModel, table=True):
    __tablename__ = "updates"

    id: Optional[int] = Field(default=None, primary_key=True)
    title: str = Field(sa_column_kwargs={"unique": False})
    description: Optional[str] = Field(default=None)
    status: str = Field(default="pending")  # pending, in-progress, completed, failed
    version: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    applied_at: Optional[datetime] = Field(default=None)
    rollback_possible: bool = Field(default=True)

    # Relationship to update logs
    logs: list["UpdateLog"] = Relationship(back_populates="update")


class UpdateLog(SQLModel, table=True):
    __tablename__ = "update_logs"

    id: Optional[int] = Field(default=None, primary_key=True)
    update_id: int = Field(foreign_key="updates.id")
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    level: str  # info, warning, error, critical
    message: str
    component: Optional[str] = Field(default=None)

    # Relationship to update
    update: Update = Relationship(back_populates="logs")


# Pydantic models for Task (separate from SQLModel)
class TaskBasePydantic(BaseModel):
    title: str
    description: Optional[str] = None
    completed: bool = False
    user_id: int


class TaskCreate(TaskBasePydantic):
    pass


class TaskRead(TaskBasePydantic):
    id: int
    created_at: datetime
    updated_at: datetime


class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None


class TaskComplete(BaseModel):
    completed: bool


# SQLModel for database (separate from Pydantic)
class Task(SQLModel, table=True):
    __tablename__ = "tasks"

    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    description: Optional[str] = Field(default=None)
    completed: bool = Field(default=False)
    user_id: int = Field(foreign_key="users.id")
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)