from service.dai_ly_DAO import get_daily_by_id
from service.hang_hoa_DAO import get_hanghoa_by_id
from service.kho_DAO import get_kho_by_id
from service.nhan_vien_DAO import get_nhanvien_by_id
from service.phieu_xuat_DAO import get_phieuxuat_by_id
from sqlalchemy.orm import Session
from model.pxhh import PhieuXuatHangHoa
from schemas.pxhh_sm import PhieuXuatHangHoaCreate, PhieuXuatHangHoaUpdate

def get_phieuxuat_hanghoas(db: Session):
    return db.query(PhieuXuatHangHoa).all()

def create_phieuxuat_hanghoa(db: Session, phieuxuat_hanghoa: PhieuXuatHangHoaCreate):
    db_phieuxuat_hanghoa = PhieuXuatHangHoa(**phieuxuat_hanghoa.dict())
    db.add(db_phieuxuat_hanghoa)
    db.commit()
    db.refresh(db_phieuxuat_hanghoa)
    return db_phieuxuat_hanghoa

def update_phieuxuat_hanghoa(db: Session, phieuxuat_hanghoa_id: int, phieuxuat_hanghoa: PhieuXuatHangHoaUpdate):
    db_phieuxuat_hanghoa = db.query(PhieuXuatHangHoa).filter(PhieuXuatHangHoa.id == phieuxuat_hanghoa_id).first()
    if db_phieuxuat_hanghoa is None:
        return None
    for key, value in phieuxuat_hanghoa.dict(exclude_unset=True).items():
        setattr(db_phieuxuat_hanghoa, key, value)
    db.commit()
    db.refresh(db_phieuxuat_hanghoa)
    return db_phieuxuat_hanghoa

def delete_phieuxuat_hanghoa(db: Session, phieuxuat_hanghoa_id: int):
    db_phieuxuat_hanghoa = db.query(PhieuXuatHangHoa).filter(PhieuXuatHangHoa.id == phieuxuat_hanghoa_id).first()
    if db_phieuxuat_hanghoa:
        db.delete(db_phieuxuat_hanghoa)
        db.commit()
    return db_phieuxuat_hanghoa

def get_pxhh_by_idPhieuXuat(db: Session, phieuxuat_id: int):
    phieuxuat = get_phieuxuat_by_id(db, phieuxuat_id)
    result = vars(phieuxuat)
    nhanvien = get_nhanvien_by_id(db, phieuxuat.idNvien)
    kho = get_kho_by_id(db, phieuxuat.idKho)
    daily = get_daily_by_id(db, phieuxuat.idDaily)
    result["nhanvien"] = nhanvien
    result["kho"] = kho
    result["daily"] = daily
    dsHangHoa = []
    pxhh = db.query(PhieuXuatHangHoa).filter(PhieuXuatHangHoa.idPx == phieuxuat_id).all()
    for item in pxhh:
        hanghoa = get_hanghoa_by_id(db, item.idHanghoa)
        new_hanghoa = vars(hanghoa)
        new_hanghoa["soluong"] = item.soluong
        new_hanghoa["dongia"] = item.dongia
        dsHangHoa.append(new_hanghoa)
    result["dsHangHoa"] = dsHangHoa
    return result
