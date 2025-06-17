"""Application entry point for the FastAPI example project."""

# FastAPI provides the web framework used throughout the project
from fastapi import FastAPI

# Import routers that expose authentication and item related endpoints
from .routers import auth, items

# Database metadata and engine are required to create tables on startup
from .database import Base, engine

# Create the FastAPI application instance
app = FastAPI()


@app.on_event("startup")
def on_startup() -> None:
    """Create database tables when the application starts."""
    Base.metadata.create_all(bind=engine)

# Register API routers for authentication and item resources
app.include_router(auth.router)
app.include_router(items.router)


@app.get("/")
async def read_root() -> dict:
    """Basic health check endpoint."""
    return {"message": "Hello World"}

