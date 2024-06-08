from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from dbconnect import Base

class PhieuBaoCaoHangHoa(Base):
    __tablename__ = 'bchh'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    idPbc = Column(Integer, ForeignKey('phieubaocao.id'), nullable=False)
    idHanghoa = Column(Integer, ForeignKey('hanghoa.id'), nullable=False)
    slban = Column(Integer, nullable=False)
    tongtien = Column(Integer, nullable=False)
