from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from service.phieu_bao_cao_DAO import get_phieubaocaos, create_phieubaocao, update_phieubaocao, delete_phieubaocao
from schemas.phieu_bao_cao_sm import PhieuBaoCao, PhieuBaoCaoCreate, PhieuBaoCaoUpdate
from dbconnect import SessionLocal

router = APIRouter()

# Dependency để lấy session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/phieubaocaos/", response_model=List[PhieuBaoCao], tags=["Phiếu báo cáo"])
def read_phieubaocaos(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    phieubaocaos = get_phieubaocaos(db, skip=skip, limit=limit)
    return phieubaocaos

@router.post("/phieubaocaos/", response_model=PhieuBaoCao, tags=["Phiếu báo cáo"])
def create_phieubaocao_endpoint(phieubaocao: PhieuBaoCaoCreate, db: Session = Depends(get_db)):
    return create_phieubaocao(db, phieubaocao)

@router.put("/phieubaocaos/{phieubaocao_id}", response_model=PhieuBaoCao, tags=["Phiếu báo cáo"])
def update_phieubaocao_endpoint(phieubaocao_id: int, phieubaocao: PhieuBaoCaoUpdate, db: Session = Depends(get_db)):
    db_phieubaocao = update_phieubaocao(db, phieubaocao_id, phieubaocao)
    if db_phieubaocao is None:
        raise HTTPException(status_code=404, detail="PhieuBaoCao not found")
    return db_phieubaocao

@router.delete("/phieubaocaos/{phieubaocao_id}", response_model=PhieuBaoCao, tags=["Phiếu báo cáo"])
def delete_phieubaocao_endpoint(phieubaocao_id: int, db: Session = Depends(get_db)):
    db_phieubaocao = delete_phieubaocao(db, phieubaocao_id)
    if db_phieubaocao is None:
        raise HTTPException(status_code=404, detail="PhieuBaoCao not found")
    return db_phieubaocao
