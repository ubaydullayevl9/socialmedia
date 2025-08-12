from fastapi import FastAPI

from db import Base, engine
from api.photo_api.main import photo_router
from api.user_api.main import user_router
from api.post_api.main import post_router

app = FastAPI(docs_url="/")

Base.metadata.create_all(engine)

app.include_router(photo_router)
app.include_router(user_router)
app.include_router(post_router)

