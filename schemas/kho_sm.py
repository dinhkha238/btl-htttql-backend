from pydantic import BaseModel
from typing import Optional

class KhoBase(BaseModel):
    ten: Optional[str] = None
    diachi: Optional[str] = None

class KhoCreate(KhoBase):
    pass

class KhoUpdate(KhoBase):
    pass

class KhoInDBBase(KhoBase):
    id: int

    class Config:
        orm_mode = True

class Kho(KhoInDBBase):
    pass

class KhoInDB(KhoInDBBase):
    pass
