from datetime import date
from pydantic import BaseModel
from typing import List, Optional

from schemas.pkkhh_sm import PhieuKiemKeHangHoaCreate

class PhieuKiemKeBase(BaseModel):
    idKho: Optional[int] = None
    idNvien: Optional[int] = None
    ngaykiemke: Optional[date] = None

class PhieuKiemKeCreate(BaseModel):
    idKho: int
    idNvien: int
    ngaykiemke: str
    hanghoas: List[PhieuKiemKeHangHoaCreate]

class PhieuKiemKeUpdate(PhieuKiemKeBase):
    pass

class PhieuKiemKeInDBBase(PhieuKiemKeBase):
    id: int

    class Config:
        orm_mode = True

class PhieuKiemKe(PhieuKiemKeInDBBase):
    pass

class PhieuKiemKeInDB(PhieuKiemKeInDBBase):
    pass
