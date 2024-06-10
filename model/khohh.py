from typing import Optional
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from dbconnect import Base

class KhoHangHoa(Base):
    __tablename__ = 'khohh'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    idKho = Column(Integer, ForeignKey('kho.id'), nullable=False)
    idHanghoa = Column(Integer, ForeignKey('hanghoa.id'), nullable=False)
    soluong = Column(Integer, nullable=False)
    