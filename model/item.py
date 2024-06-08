from sqlalchemy import Column, Integer, String
from dbconnect import Base

class Item(Base):
    __tablename__ = 'items'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), index=True)  # Độ dài cụ thể cho VARCHAR
    description = Column(String(255), index=True)  # Độ dài cụ thể cho VARCHAR
