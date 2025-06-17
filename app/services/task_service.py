"""Service functions to manage Task CRUD operations."""

from sqlalchemy.orm import Session

from .. import models, schemas


def get_tasks(db: Session):
    return db.query(models.Task).all()


def create_task(db: Session, task: schemas.TaskCreate):
    db_task = models.Task(title=task.title, description=task.description)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task


def delete_task(db: Session, task_id: int):
    task = db.query(models.Task).get(task_id)
    if task:
        db.delete(task)
        db.commit()
    return task
