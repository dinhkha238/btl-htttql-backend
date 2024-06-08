from sqlalchemy.orm import Session
from model.nha_cung_cap import NhaCungCap
from schemas.nha_cung_cap_sm import NhaCungCapCreate, NhaCungCapUpdate

def get_nhacungcaps(db: Session, skip: int = 0, limit: int = 10):
    return db.query(NhaCungCap).offset(skip).limit(limit).all()

def create_nhacungcap(db: Session, nhacungcap: NhaCungCapCreate):
    db_nhacungcap = NhaCungCap(**nhacungcap.dict())
    db.add(db_nhacungcap)
    db.commit()
    db.refresh(db_nhacungcap)
    return db_nhacungcap

def update_nhacungcap(db: Session, nhacungcap_id: int, nhacungcap: NhaCungCapUpdate):
    db_nhacungcap = db.query(NhaCungCap).filter(NhaCungCap.id == nhacungcap_id).first()
    if db_nhacungcap is None:
        return None
    for key, value in nhacungcap.dict(exclude_unset=True).items():
        setattr(db_nhacungcap, key, value)
    db.commit()
    db.refresh(db_nhacungcap)
    return db_nhacungcap

def delete_nhacungcap(db: Session, nhacungcap_id: int):
    db_nhacungcap = db.query(NhaCungCap).filter(NhaCungCap.id == nhacungcap_id).first()
    if db_nhacungcap:
        db.delete(db_nhacungcap)
        db.commit()
    return db_nhacungcap

def get_nhacungcap_by_id(db: Session, nhacungcap_id: int):
    return db.query(NhaCungCap).filter(NhaCungCap.id == nhacungcap_id).first()
