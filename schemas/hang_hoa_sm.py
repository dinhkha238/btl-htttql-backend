from pydantic import BaseModel
from typing import Optional

class HangHoaBase(BaseModel):
    ten: Optional[str] = None
    loai: Optional[str] = None
    kichthuoc: Optional[str] = None
    baohanh: Optional[str] = None
    thuonghieu: Optional[str] = None
    nguyenlieu: Optional[str] = None
    xuatxu: Optional[str] = None
    trongluong: Optional[str] = None
    mota: Optional[str] = None

class HangHoaCreate(HangHoaBase):
    pass

class HangHoaUpdate(HangHoaBase):
    pass

class HangHoaInDBBase(HangHoaBase):
    id: int

    class Config:
        orm_mode = True

class HangHoa(HangHoaInDBBase):
    pass

class HangHoaInDB(HangHoaInDBBase):
    pass
