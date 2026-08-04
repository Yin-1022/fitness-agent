from fastapi import FastAPI, Depends
from sqlalchemy import text
from sqlalchemy.orm import Session

from app.core.config import settings
from app.database.init_db import init_db
from app.database.session import get_db

app = FastAPI(
    title="Fitness Agent API",
    description="Backend API for personal fitness and body status tracking agent.",
    version="0.1.0",
)

@app.on_event("startup")
def on_startup():
    init_db()

@app.get("/")
def root():
    return {
        "message": "Fitness Agent API is running",
        "version": "0.1.0",
    }

@app.get("/health")
def health_check():
    return {
        "status": "ok",
    }

@app.get("/health/db")
def db_health_check(db: Session = Depends(get_db)):
    db.execute(text("SELECT 1"))
    return {
        "database": "ok",
    }