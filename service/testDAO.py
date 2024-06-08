from model.item import Item
from sqlalchemy.orm import Session

def get_items(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Item).offset(skip).limit(limit).all()


# Các phương thức khác cho việc thêm, sửa, xóa các item
