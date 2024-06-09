from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from service.pxhh_DAO import get_phieuxuat_hanghoas, create_phieuxuat_hanghoa, get_pxhh_by_idPhieuXuat, update_phieuxuat_hanghoa, delete_phieuxuat_hanghoa
from schemas.pxhh_sm import PhieuXuatHangHoa, PhieuXuatHangHoaCreate, PhieuXuatHangHoaUpdate
from dbconnect import SessionLocal

router = APIRouter()

# Dependency để lấy session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/phieuxuat_hanghoas/", response_model=List[PhieuXuatHangHoa], tags=["Phiếu xuất hàng hóa"])
def read_phieuxuat_hanghoas( db: Session = Depends(get_db)):
    phieuxuat_hanghoas = get_phieuxuat_hanghoas(db)
    return phieuxuat_hanghoas

@router.post("/phieuxuat_hanghoas/", response_model=PhieuXuatHangHoa, tags=["Phiếu xuất hàng hóa"])
def create_phieuxuat_hanghoa_endpoint(phieuxuat_hanghoa: PhieuXuatHangHoaCreate, db: Session = Depends(get_db)):
    return create_phieuxuat_hanghoa(db, phieuxuat_hanghoa)

@router.put("/phieuxuat_hanghoas/{phieuxuat_hanghoa_id}", response_model=PhieuXuatHangHoa, tags=["Phiếu xuất hàng hóa"])
def update_phieuxuat_hanghoa_endpoint(phieuxuat_hanghoa_id: int, phieuxuat_hanghoa: PhieuXuatHangHoaUpdate, db: Session = Depends(get_db)):
    db_phieuxuat_hanghoa = update_phieuxuat_hanghoa(db, phieuxuat_hanghoa_id, phieuxuat_hanghoa)
    if db_phieuxuat_hanghoa is None:
        raise HTTPException(status_code=404, detail="PhieuXuatHangHoa not found")
    return db_phieuxuat_hanghoa

@router.delete("/phieuxuat_hanghoas/{phieuxuat_hanghoa_id}", response_model=PhieuXuatHangHoa, tags=["Phiếu xuất hàng hóa"])
def delete_phieuxuat_hanghoa_endpoint(phieuxuat_hanghoa_id: int, db: Session = Depends(get_db)):
    db_phieuxuat_hanghoa = delete_phieuxuat_hanghoa(db, phieuxuat_hanghoa_id)
    if db_phieuxuat_hanghoa is None:
        raise HTTPException(status_code=404, detail="PhieuXuatHangHoa not found")
    return db_phieuxuat_hanghoa

@router.get("/phieuxuat_hanghoas/{phieuxuat_id}", tags=["Phiếu xuất hàng hóa"])
def read_phieuxuat(phieuxuat_id: int, db: Session = Depends(get_db)):
    phieuxuat = get_pxhh_by_idPhieuXuat(db, phieuxuat_id)
    if not phieuxuat:
        raise HTTPException(status_code=404, detail="PhieuXuat not found")
    return phieuxuat


