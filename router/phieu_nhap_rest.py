from fastapi import APIRouter, Depends, HTTPException
from schemas.pnhh_sm import PhieuNhapHangHoa
from sqlalchemy.orm import Session
from typing import List
from service.phieu_nhap_DAO import get_phieunhaps, create_phieunhap, update_phieunhap, delete_phieunhap
from schemas.phieu_nhap_sm import PhieuNhap, PhieuNhapCreate, PhieuNhapUpdate
from dbconnect import SessionLocal

router = APIRouter()

# Dependency để lấy session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/phieunhaps/", response_model=List[PhieuNhap],tags=["Phiếu nhập"])
def read_phieunhaps(db: Session = Depends(get_db)):
    phieunhaps = get_phieunhaps(db)
    return phieunhaps

@router.post("/phieunhaps/", response_model=PhieuNhap, tags=["Phiếu nhập"])
def create_phieunhap_endpoint(phieunhap: PhieuNhapCreate, db: Session = Depends(get_db)):
    return create_phieunhap(db, phieunhap)

@router.put("/phieunhaps/{phieunhap_id}", response_model=PhieuNhapHangHoa,tags=["Phiếu nhập"])
def update_phieunhap_endpoint(phieunhap_id: int, phieunhap: PhieuNhapUpdate, db: Session = Depends(get_db)):
    db_phieunhap = update_phieunhap(db, phieunhap_id, phieunhap)
    if db_phieunhap is None:
        raise HTTPException(status_code=404, detail="PhieuNhap not found")
    return db_phieunhap

@router.delete("/phieunhaps/{phieunhap_id}", response_model=PhieuNhap,tags=["Phiếu nhập"])
def delete_phieunhap_endpoint(phieunhap_id: int, db: Session = Depends(get_db)):
    db_phieunhap = delete_phieunhap(db, phieunhap_id)
    if db_phieunhap is None:
        raise HTTPException(status_code=404, detail="PhieuNhap not found")
    return db_phieunhap

