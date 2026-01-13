from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select
from typing import List
from ..database import get_session
from ..models import Task, TaskCreate, TaskRead, TaskUpdate, TaskComplete
from pydantic import ValidationError
from ..dependencies import get_current_user, validate_user_id_from_token_and_path

router = APIRouter()

@router.get("/tasks", response_model=List[TaskRead], tags=["tasks"])
def read_tasks(
    user_id: str,
    current_user: dict = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    # Validate that the user_id in the token matches the user_id in the path
    validate_user_id_from_token_and_path(current_user.user_id, user_id)
    
    # Query tasks for the specific user
    statement = select(Task).where(Task.user_id == int(user_id))
    tasks = session.exec(statement).all()
    return tasks


@router.post("/tasks", response_model=TaskRead, status_code=status.HTTP_201_CREATED, tags=["tasks"])
def create_task(
    user_id: str,
    task: TaskCreate,
    current_user: dict = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    # Validate that the user_id in the token matches the user_id in the path
    validate_user_id_from_token_and_path(current_user.user_id, user_id)

    # Create a new task
    db_task = Task.model_validate(task)
    db_task.user_id = int(user_id)
    session.add(db_task)
    session.commit()
    session.refresh(db_task)
    return db_task


@router.get("/tasks/{task_id}", response_model=TaskRead, tags=["tasks"])
def read_task(
    user_id: str,
    task_id: int,
    current_user: dict = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    # Validate that the user_id in the token matches the user_id in the path
    validate_user_id_from_token_and_path(current_user.user_id, user_id)
    
    # Query the specific task
    statement = select(Task).where(Task.id == task_id).where(Task.user_id == int(user_id))
    db_task = session.exec(statement).first()
    
    if not db_task:
        raise HTTPException(status_code=404, detail="Task not found")
    
    return db_task


@router.put("/tasks/{task_id}", response_model=TaskRead, tags=["tasks"])
def update_task(
    user_id: str,
    task_id: int,
    task_update: TaskUpdate,
    current_user: dict = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    # Validate that the user_id in the token matches the user_id in the path
    validate_user_id_from_token_and_path(current_user.user_id, user_id)
    
    # Query the specific task
    statement = select(Task).where(Task.id == task_id).where(Task.user_id == int(user_id))
    db_task = session.exec(statement).first()
    
    if not db_task:
        raise HTTPException(status_code=404, detail="Task not found")
    
    # Update the task with provided fields
    update_data = task_update.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_task, field, value)
    
    session.add(db_task)
    session.commit()
    session.refresh(db_task)
    return db_task


@router.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["tasks"])
def delete_task(
    user_id: str,
    task_id: int,
    current_user: dict = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    # Validate that the user_id in the token matches the user_id in the path
    validate_user_id_from_token_and_path(current_user.user_id, user_id)
    
    # Query the specific task
    statement = select(Task).where(Task.id == task_id).where(Task.user_id == int(user_id))
    db_task = session.exec(statement).first()
    
    if not db_task:
        raise HTTPException(status_code=404, detail="Task not found")
    
    session.delete(db_task)
    session.commit()
    return


@router.patch("/tasks/{task_id}/complete", response_model=TaskRead, tags=["tasks"])
def toggle_task_completion(
    user_id: str,
    task_id: int,
    task_complete: TaskComplete,
    current_user: dict = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    # Validate that the user_id in the token matches the user_id in the path
    validate_user_id_from_token_and_path(current_user.user_id, user_id)
    
    # Query the specific task
    statement = select(Task).where(Task.id == task_id).where(Task.user_id == int(user_id))
    db_task = session.exec(statement).first()
    
    if not db_task:
        raise HTTPException(status_code=404, detail="Task not found")
    
    # Toggle the completion status
    db_task.completed = task_complete.completed
    session.add(db_task)
    session.commit()
    session.refresh(db_task)
    return db_task