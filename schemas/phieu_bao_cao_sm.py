from datetime import date
from pydantic import BaseModel
from typing import List, Optional

from schemas.bchh_sm import PhieuBaoCaoHangHoaCreate

class PhieuBaoCaoBase(BaseModel):
    idNvien: Optional[int] = None
    idKho: Optional[int] = None
    tongslban: Optional[int] = None
    doanhthu: Optional[int] = None
    ngaybaocao: Optional[date] = None

class PhieuBaoCaoCreate(BaseModel):
    idNvien: int
    idKho: int
    ngaybaocao: str
    hanghoas: List[PhieuBaoCaoHangHoaCreate]


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
