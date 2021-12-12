from dataclasses import dataclass

@dataclass
class Order:
    uuid: str
    content: list[str]
    comment: str

    def __init__(self, uuid: str, content: list[str], comment: str):
        self.uuid = uuid
        self.content = content
        self.comment = comment
