from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from service.dai_ly_DAO import get_dailys, create_daily, update_daily, delete_daily
from schemas.dai_ly_sm import DaiLy, DaiLyCreate, DaiLyUpdate
from dbconnect import SessionLocal

router = APIRouter()

# Dependency để lấy session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/dailys/", response_model=List[DaiLy], tags=["Đại lý"])
def read_dailys(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    dailys = get_dailys(db, skip=skip, limit=limit)
    return dailys

@router.post("/dailys/", response_model=DaiLy, tags=["Đại lý"])
def create_daily_endpoint(daily: DaiLyCreate, db: Session = Depends(get_db)):
    return create_daily(db, daily)

@router.put("/dailys/{daily_id}", response_model=DaiLy, tags=["Đại lý"])
def update_daily_endpoint(daily_id: int, daily: DaiLyUpdate, db: Session = Depends(get_db)):
    db_daily = update_daily(db, daily_id, daily)
    if db_daily is None:
        raise HTTPException(status_code=404, detail="DaiLy not found")
    return db_daily

@router.delete("/dailys/{daily_id}", response_model=DaiLy, tags=["Đại lý"])
def delete_daily_endpoint(daily_id: int, db: Session = Depends(get_db)):
    db_daily = delete_daily(db, daily_id)
    if db_daily is None:
        raise HTTPException(status_code=404, detail="DaiLy not found")
    return db_daily
