from fastapi import FastAPI
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from dbconnect import Base,engine
from router import phieu_kiem_ke_rest
from router import dai_ly_rest
from router import pxhh_rest
from router import phieu_xuat_rest
from router import nhan_vien_rest
from router import kho_rest
from router import nha_cung_cap_rest
from router import pnhh_rest
from router import hang_hoa_rest
from router import phieu_nhap_rest
from router import phieu_bao_cao_rest
from router import pkkhh_rest
from router import bchh_rest

# Tạo bảng trong cơ sở dữ liệu
Base.metadata.create_all(bind=engine)

# Khởi tạo ứng dụng FastAPI
app = FastAPI()

app.include_router(pkkhh_rest.router)
app.include_router(bchh_rest.router)
app.include_router(phieu_bao_cao_rest.router)
app.include_router(phieu_kiem_ke_rest.router)
app.include_router(dai_ly_rest.router)
app.include_router(pxhh_rest.router)
app.include_router(phieu_xuat_rest.router)
app.include_router(nhan_vien_rest.router)
app.include_router(kho_rest.router)
app.include_router(nha_cung_cap_rest.router)
app.include_router(pnhh_rest.router)
app.include_router(hang_hoa_rest.router)
app.include_router(phieu_nhap_rest.router)

# Add CORS middleware to allow all origins
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)