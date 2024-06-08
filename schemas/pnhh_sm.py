from pydantic import BaseModel
from typing import Optional

class PhieuNhapHangHoaBase(BaseModel):
    idPn: int
    idHanghoa: int
    soluong: int
    dongia: int

class PhieuNhapHangHoaCreate(PhieuNhapHangHoaBase):
    pass

class PhieuNhapHangHoaUpdate(PhieuNhapHangHoaBase):
    pass

class PhieuNhapHangHoaInDBBase(PhieuNhapHangHoaBase):
    id: int

    class Config:
        orm_mode = True
        # arbitrary_types_allowed = True  # Thêm dòng này

class PhieuNhapHangHoa(PhieuNhapHangHoaInDBBase):
    pass

class PhieuNhapHangHoaInDB(PhieuNhapHangHoaInDBBase):
    pass
