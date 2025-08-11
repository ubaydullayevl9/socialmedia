from fastapi import FastAPI
from db import Base, engine
from api.photo_api.main import photo_router

app = FastAPI(docs_url="/")

Base.metadata.create_all(engine)

app.include_router(photo_router)

