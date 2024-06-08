from sqlalchemy import Column, Integer, String, Date
from dbconnect import Base

class NhanVien(Base):
    __tablename__ = 'nhanvien'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    ten = Column(String(255), nullable=True)
    vaitro = Column(Integer, nullable=True)
    ngaysinh = Column(Date, nullable=True)
    diachi = Column(String(255), nullable=True)
    email = Column(String(255), nullable=True)
    sdt = Column(String(20), nullable=True)
    username = Column(String(255), nullable=True)
    password = Column(String(255), nullable=True)
