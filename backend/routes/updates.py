from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session
from typing import List
from datetime import datetime
from ..database import get_session
from ..models import (
    Update as UpdateModel, UpdateLog as UpdateLogModel,
    UpdateCreate, UpdateRead, UpdateUpdate, UpdateApply, UpdateRollback,
    UpdateLogCreate, UpdateLogRead
)
from ..dependencies import get_current_user
from ..services.update_service import UpdateService, UpdateLogService
from ..backend_logging import log_update_activity

router = APIRouter()

@router.get("/updates", response_model=List[UpdateRead], tags=["updates"])
def read_updates(
    current_user: dict = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    statement = select(UpdateModel)
    updates = session.exec(statement).all()
    return updates


@router.get("/updates/{update_id}", response_model=UpdateRead, tags=["updates"])
def read_update(
    update_id: int,
    current_user: dict = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    update = UpdateService.get_update(session, update_id)

    if not update:
        raise HTTPException(status_code=404, detail="Update not found")

    return update


@router.post("/updates/{update_id}/apply", response_model=UpdateApply, tags=["updates"])
def apply_update(
    update_id: int,
    current_user: dict = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    update = UpdateService.get_update(session, update_id)

    if not update:
        raise HTTPException(status_code=404, detail="Update not found")

    if update.status in ["in-progress", "completed"]:
        raise HTTPException(status_code=409, detail="Update cannot be applied due to current status")

    # Attempt to apply the update
    success = UpdateService.apply_update_logic(session, update_id)

    if success:
        # Log the successful application
        log_update_activity(update_id, "info", "Update applied successfully", "update-system")

        return UpdateApply(
            message="Update applied successfully",
            status="completed",
            applied_at=update.applied_at
        )
    else:
        # Log the failure
        log_update_activity(update_id, "error", "Update application failed", "update-system")

        raise HTTPException(status_code=500, detail="Update application failed")


@router.post("/updates/{update_id}/rollback", response_model=UpdateRollback, tags=["updates"])
def rollback_update(
    update_id: int,
    current_user: dict = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    update = UpdateService.get_update(session, update_id)

    if not update:
        raise HTTPException(status_code=404, detail="Update not found")

    if not update.rollback_possible:
        raise HTTPException(status_code=409, detail="Update cannot be rolled back")

    if update.status != "completed":
        raise HTTPException(status_code=409, detail="Update cannot be rolled back due to current status")

    # Attempt to rollback the update
    success = UpdateService.rollback_update_logic(session, update_id)

    if success:
        # Log the successful rollback
        log_update_activity(update_id, "info", "Update rolled back successfully", "update-system")

        return UpdateRollback(
            message="Update rolled back successfully",
            status="completed",
            rolled_back_at=datetime.utcnow()
        )
    else:
        # Log the failure
        log_update_activity(update_id, "error", "Update rollback failed", "update-system")

        raise HTTPException(status_code=500, detail="Update rollback failed")


@router.get("/updates/{update_id}/logs", response_model=dict, tags=["updates"])
def read_update_logs(
    update_id: int,
    level: str = None,
    limit: int = 50,
    offset: int = 0,
    current_user: dict = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    # Verify the update exists
    update = UpdateService.get_update(session, update_id)

    if not update:
        raise HTTPException(status_code=404, detail="Update not found")

    # Get logs for the update
    logs = UpdateLogService.get_logs_for_update(session, update_id, level)

    # Apply pagination manually since we're working with the list
    start_idx = offset
    end_idx = min(offset + limit, len(logs))
    paginated_logs = logs[start_idx:end_idx]

    return {
        "logs": paginated_logs,
        "total_count": len(logs),
        "limit": limit,
        "offset": offset
    }