from dataclasses import dataclass
from typing import Union

@dataclass
class Dish:
    uuid: Union[str, None]
    name: str
    price: int
    restaurant_uuid: Union[str, None]

    def __init__(
        self, name: str,
        price: int, restaurant_uuid: Union[str, None]=None,
        uuid: Union[str, None]=None
    ):
        self.uuid = uuid
        self.name = name
        self.price = price
        self.restaurant_uuid = restaurant_uuid
