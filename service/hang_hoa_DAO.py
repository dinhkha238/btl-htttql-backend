from model.hang_hoa import HangHoa
from model.hhncc import HangHoaNhaCungCap
from schemas.hang_hoa_sm import HangHoaCreate, HangHoaUpdate
from sqlalchemy.orm import Session

def get_hanghoas(db: Session):
    return db.query(HangHoa).all()

def create_hanghoa(db: Session, hanghoa: HangHoaCreate):
    db_hanghoa = HangHoa(**hanghoa.dict())
    db.add(db_hanghoa)
    db.commit()
    db.refresh(db_hanghoa)
    return db_hanghoa

def update_hanghoa(db: Session, hanghoa_id: int, hanghoa: HangHoaUpdate):
    db_hanghoa = db.query(HangHoa).filter(HangHoa.id == hanghoa_id).first()
    if db_hanghoa is None:
        return None
    for key, value in hanghoa.dict(exclude_unset=True).items():
        setattr(db_hanghoa, key, value)
    db.commit()
    db.refresh(db_hanghoa)
    return db_hanghoa

def delete_hanghoa(db: Session, hanghoa_id: int):
    db_hanghoa = db.query(HangHoa).filter(HangHoa.id == hanghoa_id).first()
    if db_hanghoa:
        db.delete(db_hanghoa)
        db.commit()
    return db_hanghoa

def get_hanghoa_by_id(db: Session, hanghoa_id: int):
    return db.query(HangHoa).filter(HangHoa.id == hanghoa_id).first()

def get_hanghoa_by_idNcc(db: Session, idNcc: int):
    db_hhncc = db.query(HangHoaNhaCungCap).filter(HangHoaNhaCungCap.idNcc == idNcc).all()
    db_hh = []
    for item in db_hhncc:
        hanghoa = get_hanghoa_by_id(db, item.idHanghoa)
        db_hh.append(hanghoa)
    return db_hh
