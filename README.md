# Cyberpunk Task Board

This repository contains a small **FastAPI** backend with a **Flask** front‑end.
The front‑end uses TailwindCSS and JavaScript to present a cyberpunk styled
interface that interacts with the API via HTTP calls.

## Features

- JWT authentication and user registration.
- SQLite database managed by SQLAlchemy.
- Modular architecture with routers and services.
- Flask blueprint for the front‑end.
- Pytest test suite covering the API and the Flask routes.

## Installation

1. Create a virtual environment and install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

2. (Optional) set the environment variable `FASTAPI_URL` for the Flask app. It
   defaults to `http://localhost:8000`.

## Running the applications

Start the FastAPI server:

```bash
uvicorn app.main:app --reload
```

In a separate terminal run the Flask front‑end:

```bash
python -m frontend.app
```

Open `http://localhost:5000` to see the task board. The API documentation is
available at `http://localhost:8000/docs`.

## Running the tests

The project includes unit and integration tests for both the API and the front
end. Execute them with:

```bash
pytest --cov
```

A coverage report will be produced in the terminal. Aim for a coverage above
90 %.

