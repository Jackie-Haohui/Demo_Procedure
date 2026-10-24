from fastapi import FastAPI
from api.products import router as products_router

app = FastAPI(title="测试项目")

# 挂载路由
app.include_router(products_router, prefix="/api/v1")