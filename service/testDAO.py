from model.item import Item
from sqlalchemy.orm import Session

def get_items(db: Session):
    return db.query(Item).all()


# Các phương thức khác cho việc thêm, sửa, xóa các item
