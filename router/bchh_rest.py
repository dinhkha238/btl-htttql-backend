from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from service.bchh_DAO import get_bchh_by_idPhieubaocao, get_phieubaocao_hanghoas, create_phieubaocao_hanghoa, update_phieubaocao_hanghoa, delete_phieubaocao_hanghoa
from schemas.bchh_sm import PhieuBaoCaoHangHoa, PhieuBaoCaoHangHoaCreate, PhieuBaoCaoHangHoaUpdate
from dbconnect import SessionLocal

router = APIRouter()

# Dependency để lấy session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/phieubaocao_hanghoas/", response_model=List[PhieuBaoCaoHangHoa], tags=["Phiếu báo cáo - Hàng hóa"])
def read_phieubaocao_hanghoas(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    phieubaocao_hanghoas = get_phieubaocao_hanghoas(db, skip=skip, limit=limit)
    return phieubaocao_hanghoas

@router.post("/phieubaocao_hanghoas/", response_model=PhieuBaoCaoHangHoa, tags=["Phiếu báo cáo - Hàng hóa"])
def create_phieubaocao_hanghoa_endpoint(phieubaocao_hanghoa: PhieuBaoCaoHangHoaCreate, db: Session = Depends(get_db)):
    return create_phieubaocao_hanghoa(db, phieubaocao_hanghoa)

@router.put("/phieubaocao_hanghoas/{phieubaocao_hanghoa_id}", response_model=PhieuBaoCaoHangHoa, tags=["Phiếu báo cáo - Hàng hóa"])
def update_phieubaocao_hanghoa_endpoint(phieubaocao_hanghoa_id: int, phieubaocao_hanghoa: PhieuBaoCaoHangHoaUpdate, db: Session = Depends(get_db)):
    db_phieubaocao_hanghoa = update_phieubaocao_hanghoa(db, phieubaocao_hanghoa_id, phieubaocao_hanghoa)
    if db_phieubaocao_hanghoa is None:
        raise HTTPException(status_code=404, detail="PhieuBaoCaoHangHoa not found")
    return db_phieubaocao_hanghoa

@router.delete("/phieubaocao_hanghoas/{phieubaocao_hanghoa_id}", response_model=PhieuBaoCaoHangHoa, tags=["Phiếu báo cáo - Hàng hóa"])
def delete_phieubaocao_hanghoa_endpoint(phieubaocao_hanghoa_id: int, db: Session = Depends(get_db)):
    db_phieubaocao_hanghoa = delete_phieubaocao_hanghoa(db, phieubaocao_hanghoa_id)
    if db_phieubaocao_hanghoa is None:
        raise HTTPException(status_code=404, detail="PhieuBaoCaoHangHoa not found")
    return db_phieubaocao_hanghoa

@router.get("/phieubaocao_hanghoas/{phieubaocao_id}", tags=["Phiếu báo cáo - Hàng hóa"])
def get_bchh_by_idPhieubaocao_endpoint(phieubaocao_id: int, db: Session = Depends(get_db)):
    phieubaocao = get_bchh_by_idPhieubaocao(db, phieubaocao_id)
    if not phieubaocao:
        raise HTTPException(status_code=404, detail="PhieuBaoCao not found")
    return phieubaocao
