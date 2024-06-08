from sqlalchemy.orm import Session
from model.nhan_vien import NhanVien
from schemas.nhan_vien_sm import NhanVienCreate, NhanVienUpdate

def get_nhanviens(db: Session, skip: int = 0, limit: int = 10):
    return db.query(NhanVien).offset(skip).limit(limit).all()

def create_nhanvien(db: Session, nhanvien: NhanVienCreate):
    db_nhanvien = NhanVien(**nhanvien.dict())
    db.add(db_nhanvien)
    db.commit()
    db.refresh(db_nhanvien)
    return db_nhanvien

def update_nhanvien(db: Session, nhanvien_id: int, nhanvien: NhanVienUpdate):
    db_nhanvien = db.query(NhanVien).filter(NhanVien.id == nhanvien_id).first()
    if db_nhanvien is None:
        return None
    for key, value in nhanvien.dict(exclude_unset=True).items():
        setattr(db_nhanvien, key, value)
    db.commit()
    db.refresh(db_nhanvien)
    return db_nhanvien

def delete_nhanvien(db: Session, nhanvien_id: int):
    db_nhanvien = db.query(NhanVien).filter(NhanVien.id == nhanvien_id).first()
    if db_nhanvien:
        db.delete(db_nhanvien)
        db.commit()
    return db_nhanvien

def get_nhanvien_by_id(db: Session, nhanvien_id: int):
    return db.query(NhanVien).filter(NhanVien.id == nhanvien_id).first()
