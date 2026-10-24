# 这是一个具体的数据实现类（模拟数据库）
class InMemoryProductRepository:
    def __init__(self) -> None:
        # 假数据库
        self.products = {
            1: {"id": 1, "name": "机械键盘", "price": 499},
            2: {"id": 2, "name": "无线鼠标", "price": 199},
        }

    async def get(self, product_id: int) -> dict | None:
        # 查字典
        return self.products.get(product_id)