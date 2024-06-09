from model.pnhh import PhieuNhapHangHoa
from sqlalchemy.orm import Session
from model.phieu_nhap import PhieuNhap
from schemas.phieu_nhap_sm import PhieuNhapCreate, PhieuNhapUpdate

def get_phieunhaps(db: Session):
    return db.query(PhieuNhap).all()

def create_phieunhap(db: Session, phieunhap: PhieuNhapCreate):
    db_phieunhap = PhieuNhap(**phieunhap.dict())
    db.add(db_phieunhap)
    db.commit()
    db.refresh(db_phieunhap)
    return db_phieunhap

def update_phieunhap(db: Session, phieunhap_id: int, phieunhap: PhieuNhapUpdate):
    db_phieunhap = db.query(PhieuNhap).filter(PhieuNhap.id == phieunhap_id).first()
    if db_phieunhap is None:
        return None
    for key, value in phieunhap.dict(exclude_unset=True).items():
        setattr(db_phieunhap, key, value)
    db.commit()
    db.refresh(db_phieunhap)
    return db_phieunhap

def delete_phieunhap(db: Session, phieunhap_id: int):
    db_phieunhap = db.query(PhieuNhap).filter(PhieuNhap.id == phieunhap_id).first()
    if db_phieunhap:
        db.delete(db_phieunhap)
        db.commit()
    return db_phieunhap

def get_phieunhap_by_id(db: Session, phieunhap_id: int):
    return db.query(PhieuNhap).filter(PhieuNhap.id == phieunhap_id).first()

def create_phieunhap(db: Session, phieunhap: PhieuNhapCreate):
    db_phieunhap = PhieuNhap(
        idNcc=phieunhap.idNcc,
        idKho=phieunhap.idKho,
        idNvien=phieunhap.idNvien,
        ngaynhap=phieunhap.ngaynhap,
        tongsl=sum(item.soluong for item in phieunhap.hanghoas),
        tongtien=sum(item.soluong * item.dongia for item in phieunhap.hanghoas),
    )
    db.add(db_phieunhap)
    db.commit()
    db.refresh(db_phieunhap)

    for hanghoa in phieunhap.hanghoas:
        db_hanghoa = PhieuNhapHangHoa(
            idPn=db_phieunhap.id,
            idHanghoa=hanghoa.idHanghoa,
            soluong=hanghoa.soluong,
            dongia=hanghoa.dongia
        )
        db.add(db_hanghoa)

    db.commit()
    db.refresh(db_phieunhap)
    return db_phieunhap
