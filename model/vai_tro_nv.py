
from typing import Optional
from pydantic import BaseModel

class VaiTroNVBase(BaseModel):
    tenvaitro: Optional[str] = None
    

class VaiTroNV(VaiTroNVBase):
    id: int

    class Config:
        orm_mode = True