from dataclasses import dataclass
from entities.Customization import Customization
from entities.weapon import Weapon
from enums.cutomizations_enum import CustomizationTypesEnum


@dataclass
class WeaponWithCustomization:
    weapon: Weapon
    customizations: dict[CustomizationTypesEnum, list[Customization]]
