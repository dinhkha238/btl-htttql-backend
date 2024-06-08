from sqlalchemy import Column, Integer, Date, ForeignKey
from sqlalchemy.orm import relationship
from dbconnect import Base

class PhieuBaoCao(Base):
    __tablename__ = 'phieubaocao'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    idNvien = Column(Integer, ForeignKey('nhanvien.id'), nullable=False)
    idKho = Column(Integer, ForeignKey('kho.id'), nullable=False)
    tongslban = Column(Integer, nullable=False)
    doanhthu = Column(Integer, nullable=False)
    ngaybaocao = Column(Date, nullable=False)
