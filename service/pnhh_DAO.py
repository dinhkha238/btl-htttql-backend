from service.hang_hoa_DAO import get_hanghoa_by_id
from service.kho_DAO import get_kho_by_id
from service.nha_cung_cap_DAO import get_nhacungcap_by_id
from service.nhan_vien_DAO import get_nhanvien_by_id
from service.phieu_nhap_DAO import get_phieunhap_by_id
from sqlalchemy.orm import Session
from model.pnhh import PhieuNhapHangHoa
from schemas.pnhh_sm import PhieuNhapHangHoaCreate, PhieuNhapHangHoaUpdate

def get_phieunhaphanghoas(db: Session, skip: int = 0, limit: int = 10):
    return db.query(PhieuNhapHangHoa).offset(skip).limit(limit).all()

def create_phieunhaphanghoa(db: Session, phieunhaphanghoa: PhieuNhapHangHoaCreate):
    db_phieunhaphanghoa = PhieuNhapHangHoa(**phieunhaphanghoa.dict())
    db.add(db_phieunhaphanghoa)
    db.commit()
    db.refresh(db_phieunhaphanghoa)
    return db_phieunhaphanghoa

def update_phieunhaphanghoa(db: Session, phieunhaphanghoa_id: int, phieunhaphanghoa: PhieuNhapHangHoaUpdate):
    db_phieunhaphanghoa = db.query(PhieuNhapHangHoa).filter(PhieuNhapHangHoa.id == phieunhaphanghoa_id).first()
    if db_phieunhaphanghoa is None:
        return None
    for key, value in phieunhaphanghoa.dict(exclude_unset=True).items():
        setattr(db_phieunhaphanghoa, key, value)
    db.commit()
    db.refresh(db_phieunhaphanghoa)
    return db_phieunhaphanghoa

def delete_phieunhaphanghoa(db: Session, phieunhaphanghoa_id: int):
    db_phieunhaphanghoa = db.query(PhieuNhapHangHoa).filter(PhieuNhapHangHoa.id == phieunhaphanghoa_id).first()
    if db_phieunhaphanghoa:
        db.delete(db_phieunhaphanghoa)
        db.commit()
    return db_phieunhaphanghoa

def get_pnhh_by_idPhieuNhap(db: Session, phieunhap_id: int):
    phieunhap = get_phieunhap_by_id(db, phieunhap_id)
    result = vars(phieunhap)
    nhanvien = get_nhanvien_by_id(db, phieunhap.idNvien)
    kho = get_kho_by_id(db, phieunhap.idKho)
    nhacungcap = get_nhacungcap_by_id(db, phieunhap.idNcc)
    result["nhanvien"] = nhanvien
    result["kho"] = kho
    result["nhacungcap"] = nhacungcap
    dsHangHoa = []
    pnhh = db.query(PhieuNhapHangHoa).filter(PhieuNhapHangHoa.idPn == phieunhap_id).all()
    for item in pnhh:
        hanghoa = get_hanghoa_by_id(db, item.idHanghoa)
        new_hanghoa = vars(hanghoa)
        new_hanghoa["soluong"] = item.soluong
        new_hanghoa["dongia"] = item.dongia
        dsHangHoa.append(new_hanghoa)
    result["dsHangHoa"] = dsHangHoa
    return result
