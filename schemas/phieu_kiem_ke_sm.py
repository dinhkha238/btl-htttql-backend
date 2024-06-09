from datetime import date
from pydantic import BaseModel
from typing import Optional

class PhieuKiemKeBase(BaseModel):
    idKho: Optional[int] = None
    idNvien: Optional[int] = None
    ngaykiemke: Optional[date] = None

class PhieuKiemKeCreate(PhieuKiemKeBase):
    pass

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
