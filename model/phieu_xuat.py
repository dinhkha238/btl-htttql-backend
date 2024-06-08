from sqlalchemy import Column, Integer, String, Date
from dbconnect import Base

class PhieuXuat(Base):
    __tablename__ = 'phieuxuat'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    idDaily = Column(Integer, nullable=True)
    idKho = Column(Integer, nullable=True)
    idNVien = Column(Integer, nullable=True)
    tongsl = Column(Integer, nullable=True)
    tongtien = Column(Integer, nullable=True)
    ngayxuat = Column(Date, nullable=True)
