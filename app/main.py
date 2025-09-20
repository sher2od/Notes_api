from fastapi import FastAPI
from .routers import notes

from .database import engine,Base


# Jadvallarni yaratish
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Notes API")

# Notes routerini ulash
app.include_router(notes.router)
