# Fitness Agent Backend

This is the backend service for the Personal Fitness & Body Status Agent.

## Tech Stack

- FastAPI
- SQLite / PostgreSQL
- Clean Architecture
- TDD

## Project Structure

```text
app/
├── main.py
├── core/
├── database/
├── features/
│   ├── health_log/
│   ├── dashboard/
│   ├── profile/
│   ├── recommendation/
│   └── progress/
└── tests/

## Run Server
    uvicorn app.main:app --reload
    
## API Docs
    http://127.0.0.1:8000/docs