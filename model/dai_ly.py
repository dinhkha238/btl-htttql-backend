from sqlalchemy import Column, Integer, String
from dbconnect import Base

class DaiLy(Base):
    __tablename__ = 'daily'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    ten = Column(String(255), nullable=True)
    sdt = Column(String(20), nullable=True)
    diachi = Column(String(255), nullable=True)
