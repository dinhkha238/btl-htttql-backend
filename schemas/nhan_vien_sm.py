from datetime import date
from pydantic import BaseModel
from typing import Optional

class NhanVienBase(BaseModel):
    ten: Optional[str] = None
    vaitro: Optional[int] = None
    ngaysinh: Optional[date] = None
    diachi: Optional[str] = None
    email: Optional[str] = None
    sdt: Optional[str] = None
    username: Optional[str] = None
    password: Optional[str] = None

class NhanVienCreate(NhanVienBase):
    pass

class NhanVienUpdate(NhanVienBase):
    pass

class NhanVienInDBBase(NhanVienBase):
    id: int

    class Config:
        orm_mode = True

class NhanVien(NhanVienInDBBase):
    pass

class NhanVienInDB(NhanVienInDBBase):
    pass
