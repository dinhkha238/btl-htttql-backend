
from typing import Optional
from pydantic import BaseModel

class PhieuKiemKeBase(BaseModel):
    idKho: Optional[int] = None
    idNhanVien: Optional[int] = None
    ngaykiemke: Optional[str] = None
    tongslton: Optional[int] = None

class PhieuKiemKe(PhieuKiemKeBase):
    id: int

    class Config:
        orm_mode = True