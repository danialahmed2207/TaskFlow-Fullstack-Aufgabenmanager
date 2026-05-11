"""
FastAPI-Einstiegspunkt für die Aufgabenlöscher REST API.
Definiert alle Endpunkte und verknüpft das Backend mit dem Frontend.
"""
from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
import models
import schemas
import crud
from database import engine, get_db

# Datenbanktabellen automatisch erstellen
models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Aufgabenlöscher API",
    description="REST API zur Verwaltung von Aufgaben",
    version="1.0.0"
)

# CORS erlaubt Kommunikation mit dem React-Frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    """Root-Endpunkt zur API-Überprüfung."""
    return {"message": "Willkommen zur Aufgabenlöscher API", "version": "1.0.0"}


@app.get("/tasks", response_model=list[schemas.Task])
def read_tasks(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Liest alle Aufgaben aus der Datenbank."""
    return crud.get_tasks(db, skip=skip, limit=limit)


@app.get("/tasks/{task_id}", response_model=schemas.Task)
def read_task(task_id: int, db: Session = Depends(get_db)):
    """Liest eine einzelne Aufgabe anhand der ID."""
    task = crud.get_task(db, task_id=task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Aufgabe nicht gefunden")
    return task


@app.post("/tasks", response_model=schemas.Task, status_code=201)
def create_task(task: schemas.TaskCreate, db: Session = Depends(get_db)):
    """Erstellt eine neue Aufgabe."""
    return crud.create_task(db, task=task)


@app.put("/tasks/{task_id}", response_model=schemas.Task)
def update_task(task_id: int, task: schemas.TaskUpdate, db: Session = Depends(get_db)):
    """Aktualisiert eine bestehende Aufgabe (z. B. als erledigt markieren)."""
    updated = crud.update_task(db, task_id=task_id, task_update=task)
    if not updated:
        raise HTTPException(status_code=404, detail="Aufgabe nicht gefunden")
    return updated


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    """Löscht eine Aufgabe anhand der ID."""
    deleted = crud.delete_task(db, task_id=task_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Aufgabe nicht gefunden")
    return {"message": "Aufgabe erfolgreich gelöscht"}
