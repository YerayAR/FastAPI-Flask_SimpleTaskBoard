from fastapi import FastAPI

from .routers import auth, items
from .database import Base, engine

app = FastAPI()


@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)

app.include_router(auth.router)
app.include_router(items.router)


@app.get("/")
async def read_root():
    return {"message": "Hello World"}

