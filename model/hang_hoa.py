from sqlalchemy import Column, Integer, String
from dbconnect import Base

class HangHoa(Base):
    __tablename__ = 'hanghoa'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    ten = Column(String(255), nullable=True)
    loai = Column(String(255), nullable=True)
    kichthuoc = Column(String(255), nullable=True)
    baohanh = Column(String(255), nullable=True)
    thuonghieu = Column(String(255), nullable=True)
    nguyenlieu = Column(String(255), nullable=True)
    xuatxu = Column(String(255), nullable=True)
    trongluong = Column(String(255), nullable=True)
    mota = Column(String(255), nullable=True)
