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
The resulting binary will be located in the `dist/` directory.

## Running the tests

Execute the unit tests with coverage using:

```bash
pytest --cov
```

A coverage report will be printed in the terminal. Aim for a coverage above 90 %.
