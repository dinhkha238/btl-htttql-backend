from sqlalchemy.orm import Session
from model.dai_ly import DaiLy
from schemas.dai_ly_sm import DaiLyCreate, DaiLyUpdate

def get_dailys(db: Session):
    return db.query(DaiLy).all()

def create_daily(db: Session, daily: DaiLyCreate):
    db_daily = DaiLy(**daily.dict())
    db.add(db_daily)
    db.commit()
    db.refresh(db_daily)
    return db_daily

def update_daily(db: Session, daily_id: int, daily: DaiLyUpdate):
    db_daily = db.query(DaiLy).filter(DaiLy.id == daily_id).first()
    if db_daily is None:
        return None
    for key, value in daily.dict(exclude_unset=True).items():
        setattr(db_daily, key, value)
    db.commit()
    db.refresh(db_daily)
    return db_daily

def delete_daily(db: Session, daily_id: int):
    db_daily = db.query(DaiLy).filter(DaiLy.id == daily_id).first()
    if db_daily:
        db.delete(db_daily)
        db.commit()
    return db_daily

def get_daily_by_id(db: Session, daily_id: int):
    return db.query(DaiLy).filter(DaiLy.id == daily_id).first()