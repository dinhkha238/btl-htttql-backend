from sqlalchemy import Column, Integer, Date
from sqlalchemy.orm import relationship
from dbconnect import Base

class PhieuNhap(Base):
    __tablename__ = 'phieunhap'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    idNcc = Column(Integer, nullable=True)
    idKho = Column(Integer, nullable=True)
    idNvien = Column(Integer, nullable=True)
    tongsl = Column(Integer, nullable=True)
    ngaynhap = Column(Date, nullable=True)  # Độ dài cụ thể cho VARCHAR
    tongtien = Column(Integer, nullable=True)

    # # Định nghĩa quan hệ với các bảng khác (nếu có)
    # nhacungcap = relationship("NhaCungCap", back_populates="phieunhaps")
    # kho = relationship("Kho", back_populates="phieunhaps")
    # nhanvien = relationship("NhanVien", back_populates="phieunhaps")
