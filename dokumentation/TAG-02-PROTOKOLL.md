# Tagesprotokoll — Projekttag 2

**Datum:** 10. Mai 2026  
**Projekt:** Aufgabenlöscher — Fullstack-Aufgabenverwaltung  
**Entwickler:** Danial Ahmed  
**Dozentin:** annahoff-syntax

---

## 1. Tagesziele

| Nr. | Ziel | Status |
|-----|------|--------|
| 2.1 | SQLite-Datenbankverbindung herstellen | ✅ Erledigt |
| 2.2 | Datenbankmodell für Aufgaben erstellen | ✅ Erledigt |
| 2.3 | Validierungsschemas für API definieren | ✅ Erledigt |
| 2.4 | CRUD-Operationen implementieren | ✅ Erledigt |

---

## 2. Durchgeführte Arbeiten

### 2.1 Datenbankverbindung (`database.py`)

- Einrichtung von SQLAlchemy für SQLite
- Konfiguration der `Engine` mit `check_same_thread=False` für Multithreading-Kompatibilität
- Erstellung der `SessionLocal` für Datenbanktransaktionen
- Implementierung der `get_db()` Dependency-Funktion für FastAPI

**Technische Details:**
- Datenbank-URL: `sqlite:///./tasks.db`
- Verwendete Libraries: SQLAlchemy 2.0.36

### 2.2 Datenbankmodell (`models.py`)

Erstellung des `Task`-Modells mit folgenden Attributen:

| Feld | Typ | Constraints | Beschreibung |
|------|-----|-------------|--------------|
| `id` | Integer | PRIMARY KEY, INDEX | Eindeutige Identifikation |
| `title` | String | NOT NULL | Titel der Aufgabe |
| `description` | String | OPTIONAL | Beschreibung der Aufgabe |
| `completed` | Boolean | DEFAULT FALSE | Erledigungsstatus |

### 2.3 Pydantic-Schemas (`schemas.py`)

Definierte Schemas für Request- und Response-Validierung:

- `TaskBase` — Basisklasse mit gemeinsamen Feldern
- `TaskCreate` — Schema für das Erstellen neuer Aufgaben
- `TaskUpdate` — Schema für partielle Updates (alle Felder optional)
- `Task` — Vollständiges Response-Schema inklusive `id`

**Vorteil:** Typsicherheit und automatische Validierung der API-Daten.

### 2.4 CRUD-Operationen (`crud.py`)

Implementierung der vier Grundoperationen:

| Operation | Funktion | Beschreibung |
|-----------|----------|--------------|
| **C**reate | `create_task()` | Neue Aufgabe in DB einfügen |
| **R**ead | `get_tasks()` / `get_task()` | Alle oder einzelne Aufgabe lesen |
| **U**pdate | `update_task()` | Bestehende Aufgabe aktualisieren |
| **D**elete | `delete_task()` | Aufgabe anhand ID löschen |

**Besonderheit:** `update_task()` verwendet `exclude_unset=True`, damit nur übergebene Felder aktualisiert werden (partielles Update).

---

## 3. Verwendete Technologien

- Python 3.x
- SQLAlchemy 2.0.36 (ORM)
- Pydantic 2.x (Datenvalidierung)
- SQLite (Datenbank)

---

## 4. Git-Commits des Tages

```text
7093486 feat: add sqlite database connection and sqlalchemy base setup
b0d453d feat: implement sqlalchemy models and pydantic schemas
c64eb67 feat: add crud operations for task management layer
```

---

## 5. Probleme & Lösungen

| Problem | Lösung |
|---------|--------|
| SQLite erlaubt standardmäßig keine Thread-übergreifende Nutzung | `connect_args={"check_same_thread": False}` in der Engine-Konfiguration |
| Partielle Updates müssen flexibel sein | Verwendung von `model_dump(exclude_unset=True)` in Pydantic |

---

## 6. Ergebnis des Tages

Die komplette **Datenhaltungsschicht** (Layer 3) des Projekts ist fertiggestellt:

- ✅ Datenbankverbindung steht
- ✅ Tabellenstruktur ist definiert
- ✅ Datenvalidierung ist implementiert
- ✅ Alle CRUD-Operationen sind funktionsfähig

**Nächster Schritt (Tag 3):** REST API Endpunkte mit FastAPI erstellen und mit dem Frontend verbinden.

---

## 7. Zeitaufwand

| Phase | Zeit |
|-------|------|
| Planung & Recherche | 1 Std. |
| Datenbank-Setup | 1,5 Std. |
| Modelle & Schemas | 1 Std. |
| CRUD-Implementierung | 1,5 Std. |
| Testing & Dokumentation | 1 Std. |
| **Gesamt** | **6 Std.** |

---

*Protokoll erstellt am: 13. Mai 2026*
