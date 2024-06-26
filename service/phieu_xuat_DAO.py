from model.khohh import KhoHangHoa
from model.pxhh import PhieuXuatHangHoa
from sqlalchemy.orm import Session
from model.phieu_xuat import PhieuXuat
from schemas.phieu_xuat_sm import PhieuXuatCreate, PhieuXuatUpdate

def get_phieuxuats(db: Session):
    return db.query(PhieuXuat).all()

def update_phieuxuat(db: Session, phieuxuat_id: int, phieuxuat: PhieuXuatUpdate):
    db_phieuxuat = db.query(PhieuXuatHangHoa).filter(PhieuXuatHangHoa.idPx == phieuxuat_id, PhieuXuatHangHoa.idHanghoa == phieuxuat.idHanghoa).first()
    if db_phieuxuat:
        db_phieuxuat.soluong = phieuxuat.soluong
        db_phieuxuat.dongia = phieuxuat.dongia
        db.commit()
        db.refresh(db_phieuxuat)
        # update lại tongsl và tongtien của phiếu xuất
        db_px = db.query(PhieuXuat).filter(PhieuXuat.id == phieuxuat_id).first()
        db_px.tongsl = sum(item.soluong for item in db.query(PhieuXuatHangHoa).filter(PhieuXuatHangHoa.idPx == phieuxuat_id).all())
        db_px.tongtien = sum(item.soluong * item.dongia for item in db.query(PhieuXuatHangHoa).filter(PhieuXuatHangHoa.idPx == phieuxuat_id).all())
        db.commit()
        db.refresh(db_px)
    return db_phieuxuat

def delete_phieuxuat(db: Session, phieuxuat_id: int):
    db_phieuxuat = db.query(PhieuXuat).filter(PhieuXuat.id == phieuxuat_id).first()
    if db_phieuxuat:
        db.delete(db_phieuxuat)
        db.commit()
    return db_phieuxuat

def get_phieuxuat_by_id(db: Session, phieuxuat_id: int):
    return db.query(PhieuXuat).filter(PhieuXuat.id == phieuxuat_id).first()

def create_phieuxuat(db: Session, phieuxuat: PhieuXuatCreate):
    db_phieuxuat = PhieuXuat(
        idDaily=phieuxuat.idDaily,
        idKho=phieuxuat.idKho,
        idNvien=phieuxuat.idNvien,
        ngayxuat=phieuxuat.ngayxuat,
        tongsl=sum(item.soluong for item in phieuxuat.hanghoas),
        tongtien=sum(item.soluong * item.dongia for item in phieuxuat.hanghoas),
    )
    db.add(db_phieuxuat)
    db.commit()
    db.refresh(db_phieuxuat)

    for hanghoa in phieuxuat.hanghoas:
        db_hanghoa = PhieuXuatHangHoa(
            idPx=db_phieuxuat.id,
            idHanghoa=hanghoa.idHanghoa,
            soluong=hanghoa.soluong,
            dongia=hanghoa.dongia
        )
        db.add(db_hanghoa)

        db_kho_hh = db.query(KhoHangHoa).filter(KhoHangHoa.idKho == db_phieuxuat.idKho, KhoHangHoa.idHanghoa == hanghoa.idHanghoa).first()
        db_kho_hh.soluong -= hanghoa.soluong
        
    db.commit()
    db.refresh(db_phieuxuat)
    return db_phieuxuat

