from pydantic import BaseModel
from typing import Optional

class PhieuXuatHangHoaBase(BaseModel):
    idPx: Optional[int] = None
    idHangHoa: Optional[int] = None
    soluong: Optional[int] = None
    dongia: Optional[float] = None

class PhieuXuatHangHoaCreate(PhieuXuatHangHoaBase):
    pass

class PhieuXuatHangHoaUpdate(PhieuXuatHangHoaBase):
    pass

class PhieuXuatHangHoaInDBBase(PhieuXuatHangHoaBase):
    id: int

    class Config:
        orm_mode = True

class PhieuXuatHangHoa(PhieuXuatHangHoaInDBBase):
    pass

class PhieuXuatHangHoaInDB(PhieuXuatHangHoaInDBBase):
    pass
