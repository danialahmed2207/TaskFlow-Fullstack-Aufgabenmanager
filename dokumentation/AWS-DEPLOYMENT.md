# AWS Deployment-Anleitung — Aufgabenlöscher

> Diese Anleitung beschreibt das getrennte Deployment von Frontend (S3) und Backend (Elastic Beanstalk).

---

## Voraussetzungen

- AWS CLI installiert und konfiguriert (`aws sso login --profile Danial`)
- Node.js und npm installiert
- Python und pip installiert

---

## 1. Frontend auf S3 deployen

### 1.1 Build erstellen

```bash
cd frontend
npm install
npm run build
```

→ Erzeugt den Ordner `frontend/dist/`

### 1.2 S3 Bucket erstellen

```bash
aws s3 mb s3://aufgabenloescher-frontend-$(date +%s) --profile Danial --region eu-central-1
```

### 1.3 Static Website Hosting aktivieren

```bash
aws s3 website s3://BUCKET-NAME --index-document index.html --error-document index.html --profile Danial
```

### 1.4 Dateien hochladen

```bash
aws s3 sync dist/ s3://BUCKET-NAME --profile Danial
```

### 1.5 Öffentlicher Zugriff (für Demo)

```bash
aws s3api put-bucket-policy --bucket BUCKET-NAME --policy file://s3-policy.json --profile Danial
```

**URL:** `http://BUCKET-NAME.s3-website.eu-central-1.amazonaws.com`

---

## 2. Backend auf Elastic Beanstalk deployen

### 2.1 Application erstellen

```bash
cd backend
eb init -p python-3.9 aufgabenloescher-backend --region eu-central-1 --profile Danial
```

### 2.2 Environment erstellen

```bash
eb create aufgabenloescher-env
```

### 2.3 Deployen

```bash
eb deploy
```

**URL:** Wird nach dem Deploy angezeigt (z. B. `http://aufgabenloescher-env.eu-central-1.elasticbeanstalk.com`)

---

## 3. CORS anpassen

Nach dem Deploy musst du im Backend die `allow_origins` auf die S3-URL ändern:

```python
# backend/main.py
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://BUCKET-NAME.s3-website.eu-central-1.amazonaws.com"],
    ...
)
```

---

## 4. Wichtige Hinweise

- **Kosten:** S3 und Elastic Beanstalk (Free Tier) sind in der Regel kostenlos für kleine Projekte
- **Techstarter-Sandbox:** Prüfe mit deinem Dozenten, ob bestimmte Services erlaubt sind
- **Sicherheit:** Für Produktionsumgebungen niemals `allow_origins=["*"]` verwenden

---

*Erstellt am: 13. Mai 2026*
