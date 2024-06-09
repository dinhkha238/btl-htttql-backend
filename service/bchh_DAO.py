from service.hang_hoa_DAO import get_hanghoa_by_id
from service.kho_DAO import get_kho_by_id
from service.nhan_vien_DAO import get_nhanvien_by_id
from service.phieu_bao_cao_DAO import get_phieubaocao_by_id
from sqlalchemy.orm import Session
from model.bchh import PhieuBaoCaoHangHoa
from schemas.bchh_sm import PhieuBaoCaoHangHoaCreate, PhieuBaoCaoHangHoaUpdate

def get_phieubaocao_hanghoas(db: Session, skip: int = 0, limit: int = 10):
    return db.query(PhieuBaoCaoHangHoa).offset(skip).limit(limit).all()

def create_phieubaocao_hanghoa(db: Session, phieubaocao_hanghoa: PhieuBaoCaoHangHoaCreate):
    db_phieubaocao_hanghoa = PhieuBaoCaoHangHoa(**phieubaocao_hanghoa.dict())
    db.add(db_phieubaocao_hanghoa)
    db.commit()
    db.refresh(db_phieubaocao_hanghoa)
    return db_phieubaocao_hanghoa

def update_phieubaocao_hanghoa(db: Session, phieubaocao_hanghoa_id: int, phieubaocao_hanghoa: PhieuBaoCaoHangHoaUpdate):
    db_phieubaocao_hanghoa = db.query(PhieuBaoCaoHangHoa).filter(PhieuBaoCaoHangHoa.id == phieubaocao_hanghoa_id).first()
    if db_phieubaocao_hanghoa is None:
        return None
    for key, value in phieubaocao_hanghoa.dict(exclude_unset=True).items():
        setattr(db_phieubaocao_hanghoa, key, value)
    db.commit()
    db.refresh(db_phieubaocao_hanghoa)
    return db_phieubaocao_hanghoa

def delete_phieubaocao_hanghoa(db: Session, phieubaocao_hanghoa_id: int):
    db_phieubaocao_hanghoa = db.query(PhieuBaoCaoHangHoa).filter(PhieuBaoCaoHangHoa.id == phieubaocao_hanghoa_id).first()
    if db_phieubaocao_hanghoa:
        db.delete(db_phieubaocao_hanghoa)
        db.commit()
    return db_phieubaocao_hanghoa

def get_bchh_by_idPhieubaocao(db: Session, phieubaocao_id: int):
    phieubaocao = get_phieubaocao_by_id(db, phieubaocao_id)
    result = vars(phieubaocao)
    nhanvien = get_nhanvien_by_id(db, phieubaocao.idNvien)
    kho = get_kho_by_id(db, phieubaocao.idKho)
    result["nhanvien"] = nhanvien
    result["kho"] = kho
    dsHangHoa = []
    bchh = db.query(PhieuBaoCaoHangHoa).filter(PhieuBaoCaoHangHoa.idPbc == phieubaocao_id).all()
    for item in bchh:
        hanghoa = get_hanghoa_by_id(db, item.idHanghoa)
        new_hanghoa = vars(hanghoa)
        new_hanghoa["slban"] = item.slban
        new_hanghoa["tongtien"] = item.tongtien
        dsHangHoa.append(new_hanghoa)
    result["dsHangHoa"] = dsHangHoa
    return result
