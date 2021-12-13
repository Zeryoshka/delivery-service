from pydantic import BaseModel


class RequestBaseModel(BaseModel):
    class Config:
        extra = 'forbid'

class DeliveryPriceRequestSchema(RequestBaseModel):
    start: str
    end: str

class CreateDishRequestSchema(RequestBaseModel):
    price: int
    name: str
    restaurant: str
