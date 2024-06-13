from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from service.phieu_kiem_ke_DAO import get_phieukiemkes, create_phieukiemke, update_phieukiemke, delete_phieukiemke
from schemas.phieu_kiem_ke_sm import PhieuKiemKe, PhieuKiemKeCreate, PhieuKiemKeUpdate
from dbconnect import SessionLocal

router = APIRouter()

# Dependency để lấy session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/phieukiemkes/", tags=["Phiếu kiểm kê"])
def read_phieukiemkes( db: Session = Depends(get_db)):
    phieukiemkes = get_phieukiemkes(db)
    return phieukiemkes

@router.post("/phieukiemkes/", response_model=PhieuKiemKe, tags=["Phiếu kiểm kê"])
def create_phieukiemke_endpoint(phieukiemke: PhieuKiemKeCreate, db: Session = Depends(get_db)):
    return create_phieukiemke(db, phieukiemke)

@router.put("/phieukiemkes/{phieukiemke_id}", response_model=PhieuKiemKe, tags=["Phiếu kiểm kê"])
def update_phieukiemke_endpoint(phieukiemke_id: int, phieukiemke: PhieuKiemKeUpdate, db: Session = Depends(get_db)):
    db_phieukiemke = update_phieukiemke(db, phieukiemke_id, phieukiemke)
    if db_phieukiemke is None:
        raise HTTPException(status_code=404, detail="PhieuKiemKe not found")
    return db_phieukiemke

@router.delete("/phieukiemkes/{phieukiemke_id}", response_model=PhieuKiemKe, tags=["Phiếu kiểm kê"])
def delete_phieukiemke_endpoint(phieukiemke_id: int, db: Session = Depends(get_db)):
    db_phieukiemke = delete_phieukiemke(db, phieukiemke_id)
    if db_phieukiemke is None:
        raise HTTPException(status_code=404, detail="PhieuKiemKe not found")
    return db_phieukiemke
