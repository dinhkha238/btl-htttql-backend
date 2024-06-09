from sqlalchemy.orm import Session
from model.phieu_kiem_ke import PhieuKiemKe
from schemas.phieu_kiem_ke_sm import PhieuKiemKeCreate, PhieuKiemKeUpdate

def get_phieukiemkes(db: Session):
    return db.query(PhieuKiemKe).all()

def create_phieukiemke(db: Session, phieukiemke: PhieuKiemKeCreate):
    db_phieukiemke = PhieuKiemKe(**phieukiemke.dict())
    db.add(db_phieukiemke)
    db.commit()
    db.refresh(db_phieukiemke)
    return db_phieukiemke

def update_phieukiemke(db: Session, phieukiemke_id: int, phieukiemke: PhieuKiemKeUpdate):
    db_phieukiemke = db.query(PhieuKiemKe).filter(PhieuKiemKe.id == phieukiemke_id).first()
    if db_phieukiemke is None:
        return None
    for key, value in phieukiemke.dict(exclude_unset=True).items():
        setattr(db_phieukiemke, key, value)
    db.commit()
    db.refresh(db_phieukiemke)
    return db_phieukiemke

def delete_phieukiemke(db: Session, phieukiemke_id: int):
    db_phieukiemke = db.query(PhieuKiemKe).filter(PhieuKiemKe.id == phieukiemke_id).first()
    if db_phieukiemke:
        db.delete(db_phieukiemke)
        db.commit()
    return db_phieukiemke

def get_phieukiemke_by_id(db: Session, phieukiemke_id: int):
    return db.query(PhieuKiemKe).filter(PhieuKiemKe.id == phieukiemke_id).first()