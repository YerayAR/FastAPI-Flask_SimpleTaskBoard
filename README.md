# FastAPI Simple Test

This project is a minimal FastAPI application demonstrating:

- JWT authentication
- User management with SQLAlchemy
- Data validation with Pydantic
- SQLite database
- Modular architecture (models, routers, services)
- Automatic OpenAPI documentation
- Pytest tests

## Installation

```bash
pip install -r requirements.txt
```

## Running the Application

```bash
uvicorn app.main:app --reload
```

The API documentation will be available at `http://localhost:8000/docs`.

## Running Tests

```bash
pytest
```

