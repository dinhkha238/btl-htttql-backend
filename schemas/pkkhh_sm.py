from pydantic import BaseModel
from typing import Optional

class PhieuKiemKeHangHoaBase(BaseModel):
    idPkk: Optional[int] = None
    idHanghoa: Optional[int] = None
    soluong: Optional[int] = None

class PhieuKiemKeHangHoaCreate(BaseModel):
    idHanghoa: int
    soluong: int

class PhieuKiemKeHangHoaUpdate(PhieuKiemKeHangHoaBase):
    pass

class PhieuKiemKeHangHoaInDBBase(PhieuKiemKeHangHoaBase):
    id: int

    class Config:
        orm_mode = True

class PhieuKiemKeHangHoa(PhieuKiemKeHangHoaInDBBase):
    pass

class PhieuKiemKeHangHoaInDB(PhieuKiemKeHangHoaInDBBase):
    pass
