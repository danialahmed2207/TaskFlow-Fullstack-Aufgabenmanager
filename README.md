# 🗑️ Aufgabenlöscher

Eine professionelle Fullstack-Webanwendung zur Verwaltung von Aufgaben mit CRUD-Funktionalität.

## Projektübersicht

Dieses Projekt wurde im Rahmen eines IT-Administrator-/IHK-Projekts entwickelt und demonstriert den Aufbau einer modernen 3-Schichten-Architektur:

- **Frontend:** React + Vite
- **Backend:** Python FastAPI
- **Datenbank:** SQLite

## Funktionen

- ✅ Aufgaben erstellen (Titel + Beschreibung)
- 📋 Aufgaben anzeigen (übersichtliche Liste)
- ✏️ Aufgaben als erledigt markieren
- 🗑️ Aufgaben löschen
- 💾 Datenpersistenz über SQLite
- 🔄 REST API Kommunikation über JSON

## Projektstruktur

```
aufgabenloescher/
├── backend/
│   ├── main.py           # FastAPI Einstiegspunkt
│   ├── database.py       # SQLite Verbindung
│   ├── models.py         # SQLAlchemy Modelle
│   ├── schemas.py        # Pydantic Schemas
│   ├── crud.py           # CRUD Operationen
│   └── requirements.txt  # Python Abhängigkeiten
├── frontend/
│   ├── src/
│   │   ├── App.jsx       # Hauptkomponente
│   │   ├── App.css       # Styling
│   │   └── components/   # Wiederverwendbare Komponenten
│   ├── index.html
│   └── package.json
├── .gitignore
└── README.md
```

## Voraussetzungen

- Python 3.10+
- Node.js 18+
- Git

## Installation & Start

### 1. Repository klonen

```bash
git clone https://github.com/danialahmed2207/aufgabenloescher.git
cd aufgabenloescher
```

### 2. Backend starten

```bash
cd backend
python -m venv venv
source venv/bin/activate        # macOS/Linux
# venv\Scripts\activate         # Windows
pip install -r requirements.txt
uvicorn main:app --reload
```

Das Backend läuft unter: [http://localhost:8000](http://localhost:8000)

API-Dokumentation: [http://localhost:8000/docs](http://localhost:8000/docs)

### 3. Frontend starten

```bash
cd frontend
npm install
npm run dev
```

Das Frontend läuft unter: [http://localhost:5173](http://localhost:5173)

## API Endpunkte

| Methode | Endpunkt        | Beschreibung              |
|---------|----------------|---------------------------|
| GET     | /              | Willkommensnachricht      |
| GET     | /tasks         | Alle Aufgaben abrufen     |
| GET     | /tasks/{id}    | Einzelne Aufgabe abrufen  |
| POST    | /tasks         | Neue Aufgabe erstellen    |
| PUT     | /tasks/{id}    | Aufgabe aktualisieren     |
| DELETE  | /tasks/{id}    | Aufgabe löschen           |

## Git Workflow

Das Projekt wurde mit professionellem Branching entwickelt:

- `main` — Stabile Hauptversion
- `backend-setup` — Backend Entwicklung
- `frontend-setup` — Frontend Entwicklung

## Technologien

- **Frontend:** React 19, Vite 6, CSS3
- **Backend:** FastAPI, SQLAlchemy, Pydantic, Uvicorn
- **Datenbank:** SQLite
- **Tools:** Git, GitHub, REST API

## Autor

Entwickelt für das IT-Administrator Abschlussprojekt (IHK).
