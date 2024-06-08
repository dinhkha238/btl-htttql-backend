from pydantic import BaseModel
from typing import Optional

class PhieuBaoCaoHangHoaBase(BaseModel):
    idPbc: Optional[int] = None
    idHanghoa: Optional[int] = None
    slban: Optional[int] = None
    tongtien: Optional[int] = None

class PhieuBaoCaoHangHoaCreate(PhieuBaoCaoHangHoaBase):
    pass

class PhieuBaoCaoHangHoaUpdate(PhieuBaoCaoHangHoaBase):
    pass

class PhieuBaoCaoHangHoaInDBBase(PhieuBaoCaoHangHoaBase):
    id: int

    class Config:
        orm_mode = True

class PhieuBaoCaoHangHoa(PhieuBaoCaoHangHoaInDBBase):
    pass

class PhieuBaoCaoHangHoaInDB(PhieuBaoCaoHangHoaInDBBase):
    pass
