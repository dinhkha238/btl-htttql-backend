from model.bchh import PhieuBaoCaoHangHoa
from sqlalchemy.orm import Session
from model.phieu_bao_cao import PhieuBaoCao
from schemas.phieu_bao_cao_sm import PhieuBaoCaoCreate, PhieuBaoCaoUpdate

def get_phieubaocaos(db: Session):
    return db.query(PhieuBaoCao).all()

def create_phieubaocao(db: Session, phieubaocao: PhieuBaoCaoCreate):
    db_phieubaocao = PhieuBaoCao(
        idKho=phieubaocao.idKho,
        idNvien=phieubaocao.idNvien,
        ngaybaocao=phieubaocao.ngaybaocao,
        tongslban = sum(hanghoa.slban for hanghoa in phieubaocao.hanghoas),
        doanhthu = sum(hanghoa.tongtien for hanghoa in phieubaocao.hanghoas)
    )
    db.add(db_phieubaocao)
    db.commit()
    db.refresh(db_phieubaocao)
    for hanghoa in phieubaocao.hanghoas:
        db_bchh = PhieuBaoCaoHangHoa(
            idPbc=db_phieubaocao.id,
            idHanghoa=hanghoa.idHanghoa,
            slban=hanghoa.slban,
            tongtien=hanghoa.tongtien,
            ngayxuat=hanghoa.ngayxuat
        )
        db.add(db_bchh)
    db.commit()
    db.refresh(db_phieubaocao)
    
    return db_phieubaocao

def update_phieubaocao(db: Session, phieubaocao_id: int, phieubaocao: PhieuBaoCaoUpdate):
    db_phieubaocao = db.query(PhieuBaoCao).filter(PhieuBaoCao.id == phieubaocao_id).first()
    if db_phieubaocao is None:
        return None
    for key, value in phieubaocao.dict(exclude_unset=True).items():
        setattr(db_phieubaocao, key, value)
    db.commit()
    db.refresh(db_phieubaocao)
    return db_phieubaocao

def delete_phieubaocao(db: Session, phieubaocao_id: int):
    db_phieubaocao = db.query(PhieuBaoCao).filter(PhieuBaoCao.id == phieubaocao_id).first()
    if db_phieubaocao:
        db.delete(db_phieubaocao)
        db.commit()
    return db_phieubaocao

def get_phieubaocao_by_id(db: Session, phieubaocao_id: int):
    return db.query(PhieuBaoCao).filter(PhieuBaoCao.id == phieubaocao_id).first()
