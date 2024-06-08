from datetime import date
from pydantic import BaseModel
from typing import Optional

class PhieuBaoCaoBase(BaseModel):
    idNvien: Optional[int] = None
    idKho: Optional[int] = None
    tongslban: Optional[int] = None
    doanhthu: Optional[int] = None
    ngaybaocao: Optional[date] = None

class PhieuBaoCaoCreate(PhieuBaoCaoBase):
    pass

class PhieuBaoCaoUpdate(PhieuBaoCaoBase):
    pass

class PhieuBaoCaoInDBBase(PhieuBaoCaoBase):
    id: int

    class Config:
        orm_mode = True

class PhieuBaoCao(PhieuBaoCaoInDBBase):
    pass

class PhieuBaoCaoInDB(PhieuBaoCaoInDBBase):
    pass
