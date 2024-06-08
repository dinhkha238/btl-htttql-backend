from sqlalchemy import Column, Integer, String
from dbconnect import Base

class Kho(Base):
    __tablename__ = 'kho'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    ten = Column(String(255), nullable=True)
    diachi = Column(String(255), nullable=True)
