from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from dbconnect import Base

class PhieuKiemKeHangHoa(Base):
    __tablename__ = 'pkkhh'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    idPkk = Column(Integer, ForeignKey('phieukiemke.id'), nullable=False)
    idHanghoa = Column(Integer, ForeignKey('hanghoa.id'), nullable=False)
    soluong = Column(Integer, nullable=False)
