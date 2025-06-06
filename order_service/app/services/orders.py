from sqlalchemy.ext.asyncio import AsyncSession
from datetime import datetime

from app.database import order_crud
from app.schemas import OrderSchema, OrderCreateSchema
from app.models import OrderModel, OrderToProductModel
from app.core.exceptions import SqlException, DuplicateException
from app.core.enums import OrderStatus
from app.clients import user_client, product_client


class OrderService:
    def __init__(self):
        self.crud = order_crud

    async def get_order(self, order_id: int, session: AsyncSession) -> OrderSchema:
        order = await self.crud.read(order_id, session)
        return order

    async def get_all_orders(self, session: AsyncSession) -> list[OrderSchema]:
        orders = await self.crud.read_all(session=session)
        return orders

    async def create_order(
            self, order_data: OrderCreateSchema, session: AsyncSession
    ):
        """Ищем пользователя по номеру телефона"""
        user = await user_client.get_user_by_phone(
            name=order_data.user.name,
            phone=order_data.user.phone
        )

        """Создаем моедль заказа"""
        order = OrderModel(
            user_id=user_id,
            status=OrderStatus.PENDING,
            total=product_client.get_sum_products(order_data.products),
            created_at=datetime.now()
        )
    #
    #     try:
    #         await self.crud.create(order=order, session=session)
    #     except SqlException as ex:
    #         await session.rollback()
    #         raise DuplicateException(message=str(ex))
    #     else:
    #         for item in order_data.products:
    #             product = await product_service.get_product_by_article(item.article, session)
    #
    #             order_products = OrderToProductModel(
    #                 order_id=order.id,
    #                 product_id=product.id,
    #                 quantity=item.amount,
    #             )
    #
    #             await self.crud.create()
    #
    #         return order.id


order_srv = OrderService()
