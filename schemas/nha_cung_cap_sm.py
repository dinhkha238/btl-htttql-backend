from pydantic import BaseModel
from typing import Optional

class NhaCungCapBase(BaseModel):
    ten: Optional[str] = None
    diachi: Optional[str] = None
    sdt: Optional[str] = None
    email: Optional[str] = None

class NhaCungCapCreate(NhaCungCapBase):
    pass

class NhaCungCapUpdate(NhaCungCapBase):
    pass

class NhaCungCapInDBBase(NhaCungCapBase):
    id: int

    class Config:
        orm_mode = True

class NhaCungCap(NhaCungCapInDBBase):
    pass

class NhaCungCapInDB(NhaCungCapInDBBase):
    pass
