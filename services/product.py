from dataclasses import dataclass
from typing import Protocol

# 1. 定义接口契约（什么都不干，只规定必须有 get 方法）
class ProductRepository(Protocol):
    async def get(self, product_id: int) -> dict | None:
        ...

# 2. 定义业务异常（纯业务，不涉及 HTTP）
class ProductNotFoundError(Exception):
    pass

# 3. 核心业务逻辑类
@dataclass
class ProductService:
    repository: ProductRepository

    async def get_product(self, product_id: int) -> dict:
        # 调用底层去拿数据
        product = await self.repository.get(product_id)
        if product is None:
            # 业务判断：没找到就报错
            raise ProductNotFoundError
        return product