from typing import Optional
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from dbconnect import Base

class PhieuNhapHangHoa(Base):
    __tablename__ = 'pnhh'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    idPn = Column(Integer, ForeignKey('phieunhap.id'), nullable=False)
    idHanghoa = Column(Integer, ForeignKey('hanghoa.id'), nullable=False)
    soluong = Column(Integer, nullable=False)
    dongia = Column(Integer, nullable=False)


   

