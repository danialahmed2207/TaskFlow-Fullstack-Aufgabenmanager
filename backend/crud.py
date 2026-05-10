"""
CRUD-Operationen (Create, Read, Update, Delete) für Aufgaben.
Trennt Datenbanklogik von den API-Routen (Schichtenarchitektur).
"""
from sqlalchemy.orm import Session
import models
import schemas


def get_tasks(db: Session, skip: int = 0, limit: int = 100):
    """Liest alle Aufgaben mit Pagination-Unterstützung."""
    return db.query(models.Task).offset(skip).limit(limit).all()


def get_task(db: Session, task_id: int):
    """Liest eine einzelne Aufgabe anhand der ID."""
    return db.query(models.Task).filter(models.Task.id == task_id).first()


def create_task(db: Session, task: schemas.TaskCreate):
    """Erstellt eine neue Aufgabe in der Datenbank."""
    db_task = models.Task(
        title=task.title,
        description=task.description,
        completed=task.completed
    )
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task


def update_task(db: Session, task_id: int, task_update: schemas.TaskUpdate):
    """Aktualisiert eine bestehende Aufgabe (partielles Update möglich)."""
    db_task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if not db_task:
        return None
    # Nur übergebene Felder aktualisieren
    update_data = task_update.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_task, key, value)
    db.commit()
    db.refresh(db_task)
    return db_task


def delete_task(db: Session, task_id: int):
    """Löscht eine Aufgabe anhand der ID."""
    db_task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if not db_task:
        return None
    db.delete(db_task)
    db.commit()
    return db_task
