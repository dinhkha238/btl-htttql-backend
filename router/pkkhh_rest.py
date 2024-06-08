from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from service.pkkhh_DAO import get_phieukiemke_hanghoas, create_phieukiemke_hanghoa, get_pkkhh_by_idPhieukiemke, update_phieukiemke_hanghoa, delete_phieukiemke_hanghoa
from schemas.pkkhh_sm import PhieuKiemKeHangHoa, PhieuKiemKeHangHoaCreate, PhieuKiemKeHangHoaUpdate
from dbconnect import SessionLocal

router = APIRouter()

# Dependency để lấy session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/phieukiemke_hanghoas/", response_model=List[PhieuKiemKeHangHoa], tags=["Phiếu kiểm kê - Hàng hóa"])
def read_phieukiemke_hanghoas(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    phieukiemke_hanghoas = get_phieukiemke_hanghoas(db, skip=skip, limit=limit)
    return phieukiemke_hanghoas

@router.post("/phieukiemke_hanghoas/", response_model=PhieuKiemKeHangHoa, tags=["Phiếu kiểm kê - Hàng hóa"])
def create_phieukiemke_hanghoa_endpoint(phieukiemke_hanghoa: PhieuKiemKeHangHoaCreate, db: Session = Depends(get_db)):
    return create_phieukiemke_hanghoa(db, phieukiemke_hanghoa)

@router.put("/phieukiemke_hanghoas/{phieukiemke_hanghoa_id}", response_model=PhieuKiemKeHangHoa, tags=["Phiếu kiểm kê - Hàng hóa"])
def update_phieukiemke_hanghoa_endpoint(phieukiemke_hanghoa_id: int, phieukiemke_hanghoa: PhieuKiemKeHangHoaUpdate, db: Session = Depends(get_db)):
    db_phieukiemke_hanghoa = update_phieukiemke_hanghoa(db, phieukiemke_hanghoa_id, phieukiemke_hanghoa)
    if db_phieukiemke_hanghoa is None:
        raise HTTPException(status_code=404, detail="PhieuKiemKeHangHoa not found")
    return db_phieukiemke_hanghoa

@router.delete("/phieukiemke_hanghoas/{phieukiemke_hanghoa_id}", response_model=PhieuKiemKeHangHoa, tags=["Phiếu kiểm kê - Hàng hóa"])
def delete_phieukiemke_hanghoa_endpoint(phieukiemke_hanghoa_id: int, db: Session = Depends(get_db)):
    db_phieukiemke_hanghoa = delete_phieukiemke_hanghoa(db, phieukiemke_hanghoa_id)
    if db_phieukiemke_hanghoa is None:
        raise HTTPException(status_code=404, detail="PhieuKiemKeHangHoa not found")
    return db_phieukiemke_hanghoa

@router.get("/phieukiemke_hanghoas/{phieukiemke_id}", tags=["Phiếu kiểm kê - Hàng hóa"])
def get_pkkhh_by_idPhieukiemke_endpoint(phieukiemke_id: int, db: Session = Depends(get_db)):
    phieukiemke = get_pkkhh_by_idPhieukiemke(db, phieukiemke_id)
    if not phieukiemke:
        raise HTTPException(status_code=404, detail="PhieuKiemKe not found")
    return phieukiemke