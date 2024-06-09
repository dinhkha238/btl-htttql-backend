from datetime import date
from pydantic import BaseModel
from typing import Optional,List

from model.pnhh import PhieuNhapHangHoa
from schemas.pnhh_sm import PhieuNhapHangHoaCreate

class PhieuNhapBase(BaseModel):
    idNcc: Optional[int] = None
    idKho: Optional[int] = None
    idNvien: Optional[int] = None
    tongsl: Optional[int] = None
    ngaynhap: Optional[date] = None  # Sử dụng datetime.date cho Pydantic
    tongtien: Optional[int] = None

class PhieuNhapCreate(BaseModel):
    idNcc: int
    idKho: int
    idNvien: int
    ngaynhap: str
    hanghoas: List[PhieuNhapHangHoaCreate]

class PhieuNhapUpdate(PhieuNhapBase):
    pass

class PhieuNhapInDBBase(PhieuNhapBase):
    id: int
    # phieunhaphanghoas: List[PhieuNhapHangHoa] = []
    
    class Config:
        orm_mode = True
        # arbitrary_types_allowed = True  # Thêm dòng này

class PhieuNhap(PhieuNhapInDBBase):
    pass

class PhieuNhapInDB(PhieuNhapInDBBase):
    pass
