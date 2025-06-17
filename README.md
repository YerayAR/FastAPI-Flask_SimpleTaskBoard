# FastAPI Simple Test

This project is a minimal **FastAPI** API accompanied by a **Flask** front-end. The API demonstrates:

- JWT authentication
- User management with SQLAlchemy
- Data validation with Pydantic
- SQLite database
- Modular architecture (models, routers, services)
- Automatic OpenAPI documentation
- Pytest tests

The Flask application renders HTML templates (using Jinja2, TailwindCSS and JavaScript) that consume the FastAPI service via HTTP calls.

## Installation

```bash
pip install -r requirements.txt
```

## Running the Application

```bash
uvicorn app.main:app --reload
```

### Running the Flask Front-end

Set the environment variable `FASTAPI_URL` to the URL where the FastAPI app is running (default `http://localhost:8000`). Then start the Flask development server:

```bash
python -m frontend.app
```

Open `http://localhost:5000` in your browser to see the cyberpunk task board.

The API documentation will be available at `http://localhost:8000/docs`.

## Running Tests

```bash
pytest
```

