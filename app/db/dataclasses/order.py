from typing import Union
from dataclasses import dataclass

@dataclass
class Order:
    uuid: Union[str, None]
    content: list[str]
    comment: str
    restaurant: str

    def __init__(self, content: list[str], comment: str,
        restaurant: str='Широкая на широкую', uuid: Union[str, None]=None
    ):
        self.uuid = uuid
        self.content = content
        self.comment = comment
        self.restaurant = restaurant
