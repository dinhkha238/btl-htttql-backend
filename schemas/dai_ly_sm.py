from pydantic import BaseModel
from typing import Optional

class DaiLyBase(BaseModel):
    ten: Optional[str] = None
    sdt: Optional[str] = None
    diachi: Optional[str] = None

class DaiLyCreate(DaiLyBase):
    pass

class DaiLyUpdate(DaiLyBase):
    pass

class DaiLyInDBBase(DaiLyBase):
    id: int

    class Config:
        orm_mode = True

class DaiLy(DaiLyInDBBase):
    pass

class DaiLyInDB(DaiLyInDBBase):
    pass
