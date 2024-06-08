from sqlalchemy.orm import Session
from model.phieu_xuat import PhieuXuat
from schemas.phieu_xuat_sm import PhieuXuatCreate, PhieuXuatUpdate

def get_phieuxuats(db: Session, skip: int = 0, limit: int = 10):
    return db.query(PhieuXuat).offset(skip).limit(limit).all()

def create_phieuxuat(db: Session, phieuxuat: PhieuXuatCreate):
    db_phieuxuat = PhieuXuat(**phieuxuat.dict())
    db.add(db_phieuxuat)
    db.commit()
    db.refresh(db_phieuxuat)
    return db_phieuxuat

def update_phieuxuat(db: Session, phieuxuat_id: int, phieuxuat: PhieuXuatUpdate):
    db_phieuxuat = db.query(PhieuXuat).filter(PhieuXuat.id == phieuxuat_id).first()
    if db_phieuxuat is None:
        return None
    for key, value in phieuxuat.dict(exclude_unset=True).items():
        setattr(db_phieuxuat, key, value)
    db.commit()
    db.refresh(db_phieuxuat)
    return db_phieuxuat

def delete_phieuxuat(db: Session, phieuxuat_id: int):
    db_phieuxuat = db.query(PhieuXuat).filter(PhieuXuat.id == phieuxuat_id).first()
    if db_phieuxuat:
        db.delete(db_phieuxuat)
        db.commit()
    return db_phieuxuat

def get_phieuxuat_by_id(db: Session, phieuxuat_id: int):
    return db.query(PhieuXuat).filter(PhieuXuat.id == phieuxuat_id).first()

