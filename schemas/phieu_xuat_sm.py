from datetime import date
from pydantic import BaseModel
from typing import Optional

class PhieuXuatBase(BaseModel):
    idDaily: Optional[int] = None
    idKho: Optional[int] = None
    idNVien: Optional[int] = None
    tongsl: Optional[int] = None
    tongtien: Optional[int] = None
    ngayxuat: Optional[date] = None

class PhieuXuatCreate(PhieuXuatBase):
    pass

class PhieuXuatUpdate(PhieuXuatBase):
    pass

class PhieuXuatInDBBase(PhieuXuatBase):
    id: int

    class Config:
        orm_mode = True

class PhieuXuat(PhieuXuatInDBBase):
    pass

class PhieuXuatInDB(PhieuXuatInDBBase):
    pass
