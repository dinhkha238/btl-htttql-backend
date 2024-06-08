from sqlalchemy import Column, Integer, String, Date
from dbconnect import Base

class PhieuKiemKe(Base):
    __tablename__ = 'phieukk'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    idKho = Column(Integer, nullable=True)
    idNVien = Column(Integer, nullable=True)
    ngaykiemke = Column(Date, nullable=True)