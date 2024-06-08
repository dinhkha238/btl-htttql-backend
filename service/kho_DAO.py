from sqlalchemy.orm import Session
from model.kho import Kho
from schemas.kho_sm import KhoCreate, KhoUpdate

def get_khos(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Kho).offset(skip).limit(limit).all()

def create_kho(db: Session, kho: KhoCreate):
    db_kho = Kho(**kho.dict())
    db.add(db_kho)
    db.commit()
    db.refresh(db_kho)
    return db_kho

def update_kho(db: Session, kho_id: int, kho: KhoUpdate):
    db_kho = db.query(Kho).filter(Kho.id == kho_id).first()
    if db_kho is None:
        return None
    for key, value in kho.dict(exclude_unset=True).items():
        setattr(db_kho, key, value)
    db.commit()
    db.refresh(db_kho)
    return db_kho

def delete_kho(db: Session, kho_id: int):
    db_kho = db.query(Kho).filter(Kho.id == kho_id).first()
    if db_kho:
        db.delete(db_kho)
        db.commit()
    return db_kho

def get_kho_by_id(db: Session, kho_id: int):
    return db.query(Kho).filter(Kho.id == kho_id).first()
