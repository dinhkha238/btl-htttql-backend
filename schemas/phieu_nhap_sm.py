from datetime import date
from pydantic import BaseModel
from typing import Optional,List

from model.pnhh import PhieuNhapHangHoa

class PhieuNhapBase(BaseModel):
    idNcc: Optional[int] = None
    idKho: Optional[int] = None
    idNVien: Optional[int] = None
    tongsl: Optional[int] = None
    ngaynhap: Optional[date] = None  # Sử dụng datetime.date cho Pydantic
    tongtien: Optional[int] = None

class PhieuNhapCreate(PhieuNhapBase):
    pass

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
