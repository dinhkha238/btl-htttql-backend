from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from service.hang_hoa_DAO import get_hanghoa_by_idKho, get_hanghoa_by_idNcc, get_hanghoa_for_pbchh, get_hanghoas, create_hanghoa, update_hanghoa, delete_hanghoa
from schemas.hang_hoa_sm import HangHoa, HangHoaCreate, HangHoaUpdate
from dbconnect import SessionLocal

router = APIRouter()

# Dependency để lấy session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/hanghoas/", response_model=List[HangHoa],tags=["Hàng hóa"])
def read_hanghoas( db: Session = Depends(get_db)):
    hanghoas = get_hanghoas(db)
    return hanghoas

@router.post("/hanghoas/", response_model=HangHoa,tags=["Hàng hóa"])
def create_hanghoa_endpoint(hanghoa: HangHoaCreate, db: Session = Depends(get_db)):
    return create_hanghoa(db, hanghoa)

@router.put("/hanghoas/{hanghoa_id}", response_model=HangHoa,tags=["Hàng hóa"])
def update_hanghoa_endpoint(hanghoa_id: int, hanghoa: HangHoaUpdate, db: Session = Depends(get_db)):
    db_hanghoa = update_hanghoa(db, hanghoa_id, hanghoa)
    if db_hanghoa is None:
        raise HTTPException(status_code=404, detail="HangHoa not found")
    return db_hanghoa

@router.delete("/hanghoas/{hanghoa_id}", response_model=HangHoa,tags=["Hàng hóa"])
def delete_hanghoa_endpoint(hanghoa_id: int, db: Session = Depends(get_db)):
    db_hanghoa = delete_hanghoa(db, hanghoa_id)
    if db_hanghoa is None:
        raise HTTPException(status_code=404, detail="HangHoa not found")
    return db_hanghoa

@router.get("/hanghoas-by-idNcc/{idNcc}",tags=["Hàng hóa"])
def get_hanghoa_by_idNcc_endpoint(idNcc: int, db: Session = Depends(get_db)):
    db_hhncc = get_hanghoa_by_idNcc(db, idNcc)
    return db_hhncc

@router.get("/hanghoas-by-idKho/{idKho}",tags=["Hàng hóa"])
def get_hanghoa_by_idKho_endpoint(idKho: int, db: Session = Depends(get_db)):
    db_kho_hh = get_hanghoa_by_idKho(db, idKho)
    return db_kho_hh

@router.get("/hanghoas-for-pbchh/{idKho}/{year_month}",tags=["Hàng hóa"])
def get_hanghoa_for_pbchh_endpoint(idKho: int,year_month:str, db: Session = Depends(get_db)):
    db_hh = get_hanghoa_for_pbchh(db, idKho,year_month)
    return db_hh