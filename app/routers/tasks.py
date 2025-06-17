"""Routes to manage Task resources."""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..services import auth_service, task_service
from .. import schemas

router = APIRouter(prefix="/tasks", tags=["tasks"])


@router.get("/", response_model=list[schemas.TaskRead])
def list_tasks(db: Session = Depends(auth_service.get_db)):
    """Return all tasks."""

    return task_service.get_tasks(db)


@router.post("/", response_model=schemas.TaskRead)
def create_task(task: schemas.TaskCreate, db: Session = Depends(auth_service.get_db)):
    """Create a new task and return it."""

    return task_service.create_task(db, task)


@router.delete("/{task_id}", status_code=204)
def delete_task(task_id: int, db: Session = Depends(auth_service.get_db)):
    """Remove a task from the database."""

    task = task_service.delete_task(db, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return None
