from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from service.pnhh_DAO import get_phieunhaphanghoas, create_phieunhaphanghoa, get_pnhh_by_idPhieuNhap, update_phieunhaphanghoa, delete_phieunhaphanghoa
from schemas.pnhh_sm import PhieuNhapHangHoa, PhieuNhapHangHoaCreate, PhieuNhapHangHoaUpdate
from dbconnect import SessionLocal

router = APIRouter()

# Dependency để lấy session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/phieunhaphanghoas/", response_model=List[PhieuNhapHangHoa], tags=["Phiếu nhập hàng hóa"])
def read_phieunhaphanghoas( db: Session = Depends(get_db)):
    phieunhaphanghoas = get_phieunhaphanghoas(db)
    return phieunhaphanghoas

@router.post("/phieunhaphanghoas/", response_model=PhieuNhapHangHoa, tags=["Phiếu nhập hàng hóa"])
def create_phieunhaphanghoa_endpoint(phieunhaphanghoa: PhieuNhapHangHoaCreate, db: Session = Depends(get_db)):
    return create_phieunhaphanghoa(db, phieunhaphanghoa)

@router.put("/phieunhaphanghoas/{phieunhaphanghoa_id}", response_model=PhieuNhapHangHoa, tags=["Phiếu nhập hàng hóa"])
def update_phieunhaphanghoa_endpoint(phieunhaphanghoa_id: int, phieunhaphanghoa: PhieuNhapHangHoaUpdate, db: Session = Depends(get_db)):
    db_phieunhaphanghoa = update_phieunhaphanghoa(db, phieunhaphanghoa_id, phieunhaphanghoa)
    if db_phieunhaphanghoa is None:
        raise HTTPException(status_code=404, detail="PhieuNhapHangHoa not found")
    return db_phieunhaphanghoa

@router.delete("/phieunhaphanghoas/{phieunhaphanghoa_id}", response_model=PhieuNhapHangHoa, tags=["Phiếu nhập hàng hóa"])
def delete_phieunhaphanghoa_endpoint(phieunhaphanghoa_id: int, db: Session = Depends(get_db)):
    db_phieunhaphanghoa = delete_phieunhaphanghoa(db, phieunhaphanghoa_id)
    if db_phieunhaphanghoa is None:
        raise HTTPException(status_code=404, detail="PhieuNhapHangHoa not found")
    return db_phieunhaphanghoa

@router.get("/phieunhaphanghoas/{phieunhap_id}", tags=["Phiếu nhập hàng hóa"])
def read_phieunhap(phieunhap_id: int, db: Session = Depends(get_db)):
    phieunhap = get_pnhh_by_idPhieuNhap(db, phieunhap_id)
    if not phieunhap:
        raise HTTPException(status_code=404, detail="PhieuNhap not found")
    return phieunhap
