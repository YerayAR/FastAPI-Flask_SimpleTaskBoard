# Cyberpunk Task Board

This repository contains a small **FastAPI** backend with a **Flask** front‑end. The front-end uses TailwindCSS and JavaScript to present a cyberpunk styled interface that interacts with the API via HTTP calls.

## Features

- JWT authentication and user registration.
- SQLite database managed by SQLAlchemy.
- Modular architecture with routers and services.
- Flask blueprint for the front‑end.
- Pytest test suite covering the API and the Flask routes.

## Deployment with Docker

Ensure you have Docker and Docker Compose installed. Start the entire stack with:

```bash
chmod +x run.sh
./run.sh
```

Use the following command to stop the containers:

```bash
./run.sh down
```

The Flask front‑end will be available on [http://localhost:5000](http://localhost:5000) and the FastAPI docs on [http://localhost:8000/docs](http://localhost:8000/docs).

## Manual installation

If you prefer running the applications without Docker:

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload &
python -m frontend.app
```

Set the `FASTAPI_URL` environment variable for the Flask app if the API is hosted elsewhere. It defaults to `http://localhost:8000`.

## Optional executable for the Flask front‑end

To build a standalone executable of the Flask app for offline use:

```bash
pip install pyinstaller
pyinstaller --onefile -n taskboard frontend/app.py
```

The resulting binary will be located in the `dist/` directory.

## Running the tests

Execute the unit tests with coverage using:

```bash
pytest --cov
```

A coverage report will be printed in the terminal. Aim for a coverage above 90 %.
