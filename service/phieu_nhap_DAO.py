from model.khohh import KhoHangHoa
from model.pnhh import PhieuNhapHangHoa
from sqlalchemy.orm import Session
from model.phieu_nhap import PhieuNhap
from schemas.phieu_nhap_sm import PhieuNhapCreate, PhieuNhapUpdate

def get_phieunhaps(db: Session):
    return db.query(PhieuNhap).all()

def update_phieunhap(db: Session, phieunhap_id: int, phieunhap: PhieuNhapUpdate):
    db_phieunhap = db.query(PhieuNhapHangHoa).filter(PhieuNhapHangHoa.idPn == phieunhap_id, PhieuNhapHangHoa.idHanghoa == phieunhap.idHanghoa).first()
    if db_phieunhap:
        db_phieunhap.soluong = phieunhap.soluong
        db_phieunhap.dongia = phieunhap.dongia
        db.commit()
        db.refresh(db_phieunhap)
        # update lại tongsl và tongtien của phiếu nhập
        db_pn = db.query(PhieuNhap).filter(PhieuNhap.id == phieunhap_id).first()
        db_pn.tongsl = sum(item.soluong for item in db.query(PhieuNhapHangHoa).filter(PhieuNhapHangHoa.idPn == phieunhap_id).all())
        db_pn.tongtien = sum(item.soluong * item.dongia for item in db.query(PhieuNhapHangHoa).filter(PhieuNhapHangHoa.idPn == phieunhap_id).all())
        db.commit()
        db.refresh(db_pn)

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
        db_pn_hh = PhieuNhapHangHoa(
            idPn=db_phieunhap.id,
            idHanghoa=hanghoa.idHanghoa,
            soluong=hanghoa.soluong,
            dongia=hanghoa.dongia
        )
        db.add(db_pn_hh)

        db_kho_hh = db.query(KhoHangHoa).filter(KhoHangHoa.idKho == db_phieunhap.idKho, KhoHangHoa.idHanghoa == hanghoa.idHanghoa).first()
        if db_kho_hh is None:
            db_kho_hh = KhoHangHoa(
                idKho=db_phieunhap.idKho,
                idHanghoa=hanghoa.idHanghoa,
                soluong=hanghoa.soluong
            )
            db.add(db_kho_hh)
        else:
            db_kho_hh.soluong += hanghoa.soluong

    db.commit()
    db.refresh(db_phieunhap)
    return db_phieunhap
