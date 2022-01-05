from pydantic.dataclasses import dataclass

@dataclass
class DeliveryPriceResponseSchema:
    price: int