from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select
from typing import Optional
from datetime import timedelta
from backend.database import AsyncSessionLocal
from backend.models import User, UserCreate, UserRead
from backend.dependencies import create_access_token, verify_password, get_password_hash

router = APIRouter()


@router.post("/auth/register", response_model=UserRead)
async def register_user(user_data: UserCreate):
    async with AsyncSessionLocal() as session:
        # Check if user already exists
        existing_user = await session.exec(
            select(User).where((User.email == user_data.email) | (User.username == user_data.username))
        )
        existing_user = existing_user.first()
        
        if existing_user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="User with this email or username already exists"
            )
        
        # Create new user
        hashed_password = get_password_hash(user_data.password)
        db_user = User(
            email=user_data.email,
            username=user_data.username,
            hashed_password=hashed_password
        )
        
        session.add(db_user)
        await session.commit()
        await session.refresh(db_user)
        
        return db_user


@router.post("/auth/login")
async def login_user(email: str, password: str):
    async with AsyncSessionLocal() as session:
        # Find user by email
        result = await session.exec(select(User).where(User.email == email))
        user = result.first()
        
        if not user or not verify_password(password, user.hashed_password):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect email or password",
                headers={"WWW-Authenticate": "Bearer"},
            )
        
        # Create access token
        access_token_expires = timedelta(minutes=30)  # 30 minutes expiry
        access_token = create_access_token(
            data={"sub": str(user.id)},  # Using user ID as subject
            expires_delta=access_token_expires
        )
        
        return {
            "access_token": access_token,
            "token_type": "bearer",
            "user_id": user.id,
            "username": user.username
        }