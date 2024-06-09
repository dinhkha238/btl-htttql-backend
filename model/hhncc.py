from sqlalchemy import Column, Integer, String
from dbconnect import Base

class HangHoaNhaCungCap(Base):
    __tablename__ = 'hhncc'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    idHanghoa = Column(Integer, nullable=True)
    idNcc = Column(Integer, nullable=True)
