from sqlalchemy.orm import Session
from model.phieu_bao_cao import PhieuBaoCao
from schemas.phieu_bao_cao_sm import PhieuBaoCaoCreate, PhieuBaoCaoUpdate

def get_phieubaocaos(db: Session, skip: int = 0, limit: int = 10):
    return db.query(PhieuBaoCao).offset(skip).limit(limit).all()

def create_phieubaocao(db: Session, phieubaocao: PhieuBaoCaoCreate):
    db_phieubaocao = PhieuBaoCao(**phieubaocao.dict())
    db.add(db_phieubaocao)
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
