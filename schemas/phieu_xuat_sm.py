from datetime import date
from pydantic import BaseModel
from typing import List, Optional

from schemas.pnhh_sm import PhieuNhapHangHoaCreate

class PhieuXuatBase(BaseModel):
    idDaily: Optional[int] = None
    idKho: Optional[int] = None
    idNvien: Optional[int] = None
    tongsl: Optional[int] = None
    tongtien: Optional[int] = None
    ngayxuat: Optional[date] = None

class PhieuXuatCreate(BaseModel):
    idDaily: int
    idKho: int
    idNvien: int
    ngayxuat: str
    hanghoas: List[PhieuNhapHangHoaCreate]

class PhieuXuatUpdate(BaseModel):
    idPx: int
    idHanghoa: Optional[int] = None
    soluong: Optional[int] = None
    dongia: Optional[int] = None

class PhieuXuatInDBBase(PhieuXuatBase):
    id: int

    class Config:
        orm_mode = True

class PhieuXuat(PhieuXuatInDBBase):
    pass

class PhieuXuatInDB(PhieuXuatInDBBase):
    pass
