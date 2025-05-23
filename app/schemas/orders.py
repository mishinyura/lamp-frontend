from pydantic import BaseModel, ConfigDict
from decimal import Decimal
from datetime import datetime

from app.core.enums import OrderStatus
from app.schemas.products import ProductAddCartSchema
from app.schemas.users import UserCreateSchema


class OrderSchema(BaseModel):
    id: int
    user_id: int
    status: OrderStatus
    total: Decimal
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


class OrderCreateSchema(BaseModel):
    user: UserCreateSchema
    products: list[ProductAddCartSchema]

    model_config = {
        "arbitrary_types_allowed": True
    }