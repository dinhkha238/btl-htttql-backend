from service.hang_hoa_DAO import get_hanghoa_by_id
from service.kho_DAO import get_kho_by_id
from service.nhan_vien_DAO import get_nhanvien_by_id
from service.phieu_kiem_ke_DAO import get_phieukiemke_by_id
from sqlalchemy.orm import Session
from model.pkkhh import PhieuKiemKeHangHoa
from schemas.pkkhh_sm import PhieuKiemKeHangHoaCreate, PhieuKiemKeHangHoaUpdate

def get_phieukiemke_hanghoas(db: Session, skip: int = 0, limit: int = 10):
    return db.query(PhieuKiemKeHangHoa).offset(skip).limit(limit).all()

def create_phieukiemke_hanghoa(db: Session, phieukiemke_hanghoa: PhieuKiemKeHangHoaCreate):
    db_phieukiemke_hanghoa = PhieuKiemKeHangHoa(**phieukiemke_hanghoa.dict())
    db.add(db_phieukiemke_hanghoa)
    db.commit()
    db.refresh(db_phieukiemke_hanghoa)
    return db_phieukiemke_hanghoa

def update_phieukiemke_hanghoa(db: Session, phieukiemke_hanghoa_id: int, phieukiemke_hanghoa: PhieuKiemKeHangHoaUpdate):
    db_phieukiemke_hanghoa = db.query(PhieuKiemKeHangHoa).filter(PhieuKiemKeHangHoa.id == phieukiemke_hanghoa_id).first()
    if db_phieukiemke_hanghoa is None:
        return None
    for key, value in phieukiemke_hanghoa.dict(exclude_unset=True).items():
        setattr(db_phieukiemke_hanghoa, key, value)
    db.commit()
    db.refresh(db_phieukiemke_hanghoa)
    return db_phieukiemke_hanghoa

def delete_phieukiemke_hanghoa(db: Session, phieukiemke_hanghoa_id: int):
    db_phieukiemke_hanghoa = db.query(PhieuKiemKeHangHoa).filter(PhieuKiemKeHangHoa.id == phieukiemke_hanghoa_id).first()
    if db_phieukiemke_hanghoa:
        db.delete(db_phieukiemke_hanghoa)
        db.commit()
    return db_phieukiemke_hanghoa

def get_pkkhh_by_idPhieukiemke(db: Session, phieukiemke_id: int):
    phieukiemke = get_phieukiemke_by_id(db, phieukiemke_id)
    result = vars(phieukiemke)
    nhanvien = get_nhanvien_by_id(db, phieukiemke.idNVien)
    kho = get_kho_by_id(db, phieukiemke.idKho)
    result["nhanvien"] = nhanvien
    result["kho"] = kho
    dsHangHoa = []
    pkkhh = db.query(PhieuKiemKeHangHoa).filter(PhieuKiemKeHangHoa.idPkk == phieukiemke_id).all()
    for item in pkkhh:
        hanghoa = get_hanghoa_by_id(db, item.idHanghoa)
        dsHangHoa.append(hanghoa)
    result["dsHangHoa"] = dsHangHoa
    return result
    