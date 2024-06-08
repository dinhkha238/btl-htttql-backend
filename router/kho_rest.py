from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from service.kho_DAO import get_khos, create_kho, update_kho, delete_kho
from schemas.kho_sm import Kho, KhoCreate, KhoUpdate
from dbconnect import SessionLocal

router = APIRouter()

# Dependency để lấy session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/khos/", response_model=List[Kho], tags=["Kho"])
def read_khos(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    khos = get_khos(db, skip=skip, limit=limit)
    return khos

@router.post("/khos/", response_model=Kho, tags=["Kho"])
def create_kho_endpoint(kho: KhoCreate, db: Session = Depends(get_db)):
    return create_kho(db, kho)

@router.put("/khos/{kho_id}", response_model=Kho, tags=["Kho"])
def update_kho_endpoint(kho_id: int, kho: KhoUpdate, db: Session = Depends(get_db)):
    db_kho = update_kho(db, kho_id, kho)
    if db_kho is None:
        raise HTTPException(status_code=404, detail="Kho not found")
    return db_kho

@router.delete("/khos/{kho_id}", response_model=Kho, tags=["Kho"])
def delete_kho_endpoint(kho_id: int, db: Session = Depends(get_db)):
    db_kho = delete_kho(db, kho_id)
    if db_kho is None:
        raise HTTPException(status_code=404, detail="Kho not found")
    return db_kho
