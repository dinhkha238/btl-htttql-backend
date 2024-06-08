from sqlalchemy import Column, Integer, ForeignKey, Float
from dbconnect import Base

class PhieuXuatHangHoa(Base):
    __tablename__ = 'pxhh'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    idPx = Column(Integer, ForeignKey('phieuxuat.id'), nullable=False)
    idHanghoa = Column(Integer, ForeignKey('hanghoa.id'), nullable=False)
    soluong = Column(Integer, nullable=False)
    dongia = Column(Float, nullable=False)
