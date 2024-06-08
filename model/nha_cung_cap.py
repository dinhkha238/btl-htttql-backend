from sqlalchemy import Column, Integer, String
from dbconnect import Base

class NhaCungCap(Base):
    __tablename__ = 'ncc'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    ten = Column(String(255), nullable=True)
    diachi = Column(String(255), nullable=True)
    sdt = Column(String(20), nullable=True)
    email = Column(String(255), nullable=True)
