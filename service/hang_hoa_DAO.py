from model.hang_hoa import HangHoa
from model.hhncc import HangHoaNhaCungCap
from model.khohh import KhoHangHoa
from model.phieu_xuat import PhieuXuat
from model.pxhh import PhieuXuatHangHoa
from schemas.hang_hoa_sm import HangHoaCreate, HangHoaUpdate
from sqlalchemy.orm import Session

def get_hanghoas(db: Session):
    return db.query(HangHoa).all()

def create_hanghoa(db: Session, hanghoa: HangHoaCreate):
    db_hanghoa = HangHoa(**hanghoa.dict())
    db.add(db_hanghoa)
    db.commit()
    db.refresh(db_hanghoa)
    return db_hanghoa

def update_hanghoa(db: Session, hanghoa_id: int, hanghoa: HangHoaUpdate):
    db_hanghoa = db.query(HangHoa).filter(HangHoa.id == hanghoa_id).first()
    if db_hanghoa is None:
        return None
    for key, value in hanghoa.dict(exclude_unset=True).items():
        setattr(db_hanghoa, key, value)
    db.commit()
    db.refresh(db_hanghoa)
    return db_hanghoa

def delete_hanghoa(db: Session, hanghoa_id: int):
    db_hanghoa = db.query(HangHoa).filter(HangHoa.id == hanghoa_id).first()
    if db_hanghoa:
        db.delete(db_hanghoa)
        db.commit()
    return db_hanghoa

def get_hanghoa_by_id(db: Session, hanghoa_id: int):
    return db.query(HangHoa).filter(HangHoa.id == hanghoa_id).first()

def get_hanghoa_by_idNcc(db: Session, idNcc: int):
    db_hhncc = db.query(HangHoaNhaCungCap).filter(HangHoaNhaCungCap.idNcc == idNcc).all()
    db_hh = []
    for item in db_hhncc:
        hanghoa = get_hanghoa_by_id(db, item.idHanghoa)
        db_hh.append(hanghoa)
    return db_hh

def get_hanghoa_by_idKho(db: Session, idKho: int):
    db_kho_hh = db.query(KhoHangHoa).filter(KhoHangHoa.idKho == idKho).all()
    db_hh = []
    for item in db_kho_hh:
        hanghoa = get_hanghoa_by_id(db, item.idHanghoa)
        new_hanghoa = vars(hanghoa)
        new_hanghoa['soluongton'] = item.soluong
        db_hh.append(new_hanghoa)
    return db_hh

def get_hanghoa_for_pbchh(db: Session, idKho: int,year_month:str):
    db_phieuxuat = db.query(PhieuXuat).filter(PhieuXuat.idKho == idKho,PhieuXuat.ngayxuat.startswith(year_month)).all()
    new_obj = []
    for phieuxuat in db_phieuxuat:
        phieuxuat_hanghoa = db.query(PhieuXuatHangHoa).filter(PhieuXuatHangHoa.idPx == phieuxuat.id).all()
        for item in phieuxuat_hanghoa:
            doanhthu = item.soluong * item.dongia
            if item.idHanghoa not in [hanghoa['id'] for hanghoa in new_obj]:
                hanghoa = get_hanghoa_by_id(db, item.idHanghoa)
                new_hanghoa = vars(hanghoa)
                new_hanghoa['soluongxuat'] = item.soluong
                new_hanghoa['doanhthu'] = doanhthu
                new_hanghoa['ngayxuat'] = phieuxuat.ngayxuat
                new_obj.append(new_hanghoa)
            else:
                for hanghoa in new_obj:
                    if hanghoa['id'] == item.idHanghoa:
                        hanghoa['soluongxuat'] += item.soluong
                        hanghoa['doanhthu'] += doanhthu
    return new_obj

