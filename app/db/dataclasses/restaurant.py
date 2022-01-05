from dataclasses import dataclass

@dataclass
class Restaurnat:
    uuid: str
    coords: str
    name: str

    def __init__(self, uuid: str, coords: str, name: str):
        self.name = name
        self.uuid = uuid
        self.coords = coords
