from fastapi import APIRouter, HTTPException
from dependencies import ServiceDep
from services.product import ProductNotFoundError

router = APIRouter(prefix="/products", tags=["商品"])

@router.get("/{product_id}")
async def get_product_endpoint(product_id: int, service: ServiceDep) -> dict:
    try:
        # 纯调用，不写任何 if/else 业务逻辑
        return await service.get_product(product_id)
    except ProductNotFoundError as exc:
        # 捕获业务异常，转换为 HTTP 404
        raise HTTPException(status_code=404, detail="商品不存在") from exc