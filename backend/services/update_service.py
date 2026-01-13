from sqlmodel import Session, select
from typing import Optional
from datetime import datetime
from ..models import Update as UpdateModel, UpdateLog as UpdateLogModel
from ..models import UpdateCreate, UpdateUpdate, UpdateLogCreate
from ..database import get_session


class UpdateService:
    @staticmethod
    def create_update(session: Session, update_data: UpdateCreate) -> UpdateModel:
        """Create a new update record"""
        update = UpdateModel(
            title=update_data.title,
            description=update_data.description,
            version=update_data.version,
            status="pending"
        )
        session.add(update)
        session.commit()
        session.refresh(update)
        return update
    
    @staticmethod
    def get_update(session: Session, update_id: int) -> Optional[UpdateModel]:
        """Get an update by ID"""
        statement = select(UpdateModel).where(UpdateModel.id == update_id)
        return session.exec(statement).first()
    
    @staticmethod
    def update_update(session: Session, update_id: int, update_data: UpdateUpdate) -> Optional[UpdateModel]:
        """Update an existing update record"""
        update = UpdateService.get_update(session, update_id)
        if not update:
            return None
        
        update_update_data = update_data.dict(exclude_unset=True)
        for field, value in update_update_data.items():
            setattr(update, field, value)
        
        update.updated_at = datetime.utcnow()
        session.add(update)
        session.commit()
        session.refresh(update)
        return update
    
    @staticmethod
    def delete_update(session: Session, update_id: int) -> bool:
        """Delete an update by ID"""
        update = UpdateService.get_update(session, update_id)
        if not update:
            return False
        
        session.delete(update)
        session.commit()
        return True
    
    @staticmethod
    def apply_update_logic(session: Session, update_id: int) -> bool:
        """Apply the actual update logic (placeholder implementation)"""
        update = UpdateService.get_update(session, update_id)
        if not update:
            return False
        
        # In a real implementation, this would contain the actual update logic
        # For now, we'll just simulate the process
        
        # Update status to in-progress
        update.status = "in-progress"
        update.updated_at = datetime.utcnow()
        session.add(update)
        session.commit()
        
        # Simulate the update process
        try:
            # Actual update logic would go here
            # For example: schema migrations, data transformations, etc.
            
            # Update status to completed
            update.status = "completed"
            update.applied_at = datetime.utcnow()
            update.updated_at = datetime.utcnow()
            session.add(update)
            session.commit()
            
            return True
        except Exception as e:
            # If there's an error, mark as failed
            update.status = "failed"
            update.updated_at = datetime.utcnow()
            session.add(update)
            session.commit()
            
            # Log the error
            from backend.backend_logging import log_update_activity
            log_update_activity(update_id, "error", f"Update failed: {str(e)}", "update-service")
            
            return False
    
    @staticmethod
    def rollback_update_logic(session: Session, update_id: int) -> bool:
        """Rollback an update (placeholder implementation)"""
        update = UpdateService.get_update(session, update_id)
        if not update:
            return False
        
        if not update.rollback_possible:
            return False
        
        if update.status != "completed":
            return False
        
        # Update status to in-progress (for rollback)
        update.status = "in-progress"
        update.updated_at = datetime.utcnow()
        session.add(update)
        session.commit()
        
        # Simulate the rollback process
        try:
            # Actual rollback logic would go here
            # For example: reverse schema migrations, data restoration, etc.
            
            # Update status to completed (meaning rollback is complete)
            update.status = "completed"
            update.applied_at = None  # Clear applied_at since we've rolled back
            update.updated_at = datetime.utcnow()
            session.add(update)
            session.commit()
            
            return True
        except Exception as e:
            # If there's an error, mark as failed
            update.status = "failed"
            update.updated_at = datetime.utcnow()
            session.add(update)
            session.commit()
            
            # Log the error
            from backend.backend_logging import log_update_activity
            log_update_activity(update_id, "error", f"Rollback failed: {str(e)}", "update-service")
            
            return False


class UpdateLogService:
    @staticmethod
    def create_log(session: Session, log_data: UpdateLogCreate) -> UpdateLogModel:
        """Create a new update log entry"""
        log_entry = UpdateLogModel(
            update_id=log_data.update_id,
            level=log_data.level,
            message=log_data.message,
            component=log_data.component
        )
        session.add(log_entry)
        session.commit()
        session.refresh(log_entry)
        return log_entry
    
    @staticmethod
    def get_logs_for_update(session: Session, update_id: int, level: str = None) -> list[UpdateLogModel]:
        """Get all logs for a specific update"""
        statement = select(UpdateLogModel).where(UpdateLogModel.update_id == update_id)
        
        if level:
            statement = statement.where(UpdateLogModel.level == level)
        
        statement = statement.order_by(UpdateLogModel.timestamp.desc())
        return session.exec(statement).all()