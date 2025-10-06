# StockTrainer (Flask)

A Flask backend to serve the existing static HTML project and wire up basic auth flows.

## Quickstart

1) Create a virtual environment (recommended)

- Windows (PowerShell)
```
python -m venv .venv
.venv\Scripts\Activate.ps1
```

2) Install dependencies
```
pip install -r requirements.txt
```

3) Run the server
```
python app.py
```
The app runs on http://127.0.0.1:5000

## What’s included
- `app.py`: Flask app that serves all top-level HTML, static files, and demo auth endpoints (`/login`, `/signup`, `/logout`).
- `requirements.txt`: Python deps.
- Uses the project root as both templates and static folder so you don’t need to move files.

## Notes
- Demo-only auth: submissions on Login/Signup simply set a session value and redirect to `profile.html`. Replace with real auth when ready.
- All assets referenced by relative paths (images, CSS from CDNs) are served directly.
- Any `*.html` at project root is available at `/<name>.html`.

## Environment
Optionally set:
```
set FLASK_SECRET_KEY=change-me
set FLASK_RUN_HOST=0.0.0.0
set FLASK_RUN_PORT=5000
set FLASK_DEBUG=1
```
