from fastapi import Depends
from typing import Annotated

# 导入底层的实现类
from repositories.product import InMemoryProductRepository
# 导入接口和业务类
from services.product import ProductRepository, ProductService

# 1. 实例化唯一的底层对象（全项目共享）
_product_repo_instance = InMemoryProductRepository()

# 2. 提供 Repo 的工厂函数
def get_product_repository() -> ProductRepository:
    return _product_repo_instance

# 3. 提供 Service 的工厂函数（自动获取上面的 Repo 并塞进去）
def get_product_service(
    repo: Annotated[ProductRepository, Depends(get_product_repository)]
) -> ProductService:
    return ProductService(repository=repo)

# 4. 定义快捷别名，方便路由层使用
ServiceDep = Annotated[ProductService, Depends(get_product_service)]