from fastapi import FastAPI
from . import models
from .database import engine
from .routers import qotd

app = FastAPI()

app.include_router(qotd.router)

models.Base.metadata.create_all(bind=engine)
