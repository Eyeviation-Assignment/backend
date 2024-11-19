from dataclasses import dataclass
from enums.weapons_enum import WeaponsEnum


@dataclass
class Weapon:
    model: WeaponsEnum
    id: str
