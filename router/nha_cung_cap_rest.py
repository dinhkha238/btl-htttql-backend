from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from service.nha_cung_cap_DAO import get_nhacungcaps, create_nhacungcap, update_nhacungcap, delete_nhacungcap
from schemas.nha_cung_cap_sm import NhaCungCap, NhaCungCapCreate, NhaCungCapUpdate
from dbconnect import SessionLocal

router = APIRouter()

# Dependency để lấy session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/nhacungcaps/", response_model=List[NhaCungCap], tags=["Nhà cung cấp"])
def read_nhacungcaps(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    nhacungcaps = get_nhacungcaps(db, skip=skip, limit=limit)
    return nhacungcaps

@router.post("/nhacungcaps/", response_model=NhaCungCap, tags=["Nhà cung cấp"])
def create_nhacungcap_endpoint(nhacungcap: NhaCungCapCreate, db: Session = Depends(get_db)):
    return create_nhacungcap(db, nhacungcap)

@router.put("/nhacungcaps/{nhacungcap_id}", response_model=NhaCungCap, tags=["Nhà cung cấp"])
def update_nhacungcap_endpoint(nhacungcap_id: int, nhacungcap: NhaCungCapUpdate, db: Session = Depends(get_db)):
    db_nhacungcap = update_nhacungcap(db, nhacungcap_id, nhacungcap)
    if db_nhacungcap is None:
        raise HTTPException(status_code=404, detail="NhaCungCap not found")
    return db_nhacungcap

@router.delete("/nhacungcaps/{nhacungcap_id}", response_model=NhaCungCap, tags=["Nhà cung cấp"])
def delete_nhacungcap_endpoint(nhacungcap_id: int, db: Session = Depends(get_db)):
    db_nhacungcap = delete_nhacungcap(db, nhacungcap_id)
    if db_nhacungcap is None:
        raise HTTPException(status_code=404, detail="NhaCungCap not found")
    return db_nhacungcap
