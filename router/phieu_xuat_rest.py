from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from service.phieu_xuat_DAO import get_phieuxuats, create_phieuxuat, update_phieuxuat, delete_phieuxuat
from schemas.phieu_xuat_sm import PhieuXuat, PhieuXuatCreate, PhieuXuatUpdate
from dbconnect import SessionLocal

router = APIRouter()

# Dependency để lấy session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/phieuxuats/", response_model=List[PhieuXuat], tags=["Phiếu xuất"])
def read_phieuxuats( db: Session = Depends(get_db)):
    phieuxuats = get_phieuxuats(db)
    return phieuxuats

@router.post("/phieuxuats/", response_model=PhieuXuat, tags=["Phiếu xuất"])
def create_phieuxuat_endpoint(phieuxuat: PhieuXuatCreate, db: Session = Depends(get_db)):
    return create_phieuxuat(db, phieuxuat)

@router.put("/phieuxuats/{phieuxuat_id}", response_model=PhieuXuat, tags=["Phiếu xuất"])
def update_phieuxuat_endpoint(phieuxuat_id: int, phieuxuat: PhieuXuatUpdate, db: Session = Depends(get_db)):
    db_phieuxuat = update_phieuxuat(db, phieuxuat_id, phieuxuat)
    if db_phieuxuat is None:
        raise HTTPException(status_code=404, detail="PhieuXuat not found")
    return db_phieuxuat

@router.delete("/phieuxuats/{phieuxuat_id}", response_model=PhieuXuat, tags=["Phiếu xuất"])
def delete_phieuxuat_endpoint(phieuxuat_id: int, db: Session = Depends(get_db)):
    db_phieuxuat = delete_phieuxuat(db, phieuxuat_id)
    if db_phieuxuat is None:
        raise HTTPException(status_code=404, detail="PhieuXuat not found")
    return db_phieuxuat
