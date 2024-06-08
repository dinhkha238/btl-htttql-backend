from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from service.nhan_vien_DAO import get_nhanviens, create_nhanvien, update_nhanvien, delete_nhanvien
from schemas.nhan_vien_sm import NhanVien, NhanVienCreate, NhanVienUpdate
from dbconnect import SessionLocal

router = APIRouter()

# Dependency để lấy session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/nhanviens/", response_model=List[NhanVien], tags=["Nhân viên"])
def read_nhanviens(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    nhanviens = get_nhanviens(db, skip=skip, limit=limit)
    return nhanviens

@router.post("/nhanviens/", response_model=NhanVien, tags=["Nhân viên"])
def create_nhanvien_endpoint(nhanvien: NhanVienCreate, db: Session = Depends(get_db)):
    return create_nhanvien(db, nhanvien)

@router.put("/nhanviens/{nhanvien_id}", response_model=NhanVien, tags=["Nhân viên"])
def update_nhanvien_endpoint(nhanvien_id: int, nhanvien: NhanVienUpdate, db: Session = Depends(get_db)):
    db_nhanvien = update_nhanvien(db, nhanvien_id, nhanvien)
    if db_nhanvien is None:
        raise HTTPException(status_code=404, detail="NhanVien not found")
    return db_nhanvien

@router.delete("/nhanviens/{nhanvien_id}", response_model=NhanVien, tags=["Nhân viên"])
def delete_nhanvien_endpoint(nhanvien_id: int, db: Session = Depends(get_db)):
    db_nhanvien = delete_nhanvien(db, nhanvien_id)
    if db_nhanvien is None:
        raise HTTPException(status_code=404, detail="NhanVien not found")
    return db_nhanvien
