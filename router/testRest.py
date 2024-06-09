from fastapi import APIRouter, Depends
from service.testDAO import get_items
from sqlalchemy.orm import Session
from dbconnect import SessionLocal

router = APIRouter()

# Dependency để lấy session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/items/")
def read_items( db: Session = Depends(get_db)):
    items = get_items(db)
    return items
