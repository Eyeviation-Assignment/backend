from dataclasses import dataclass, field

from entities.saved_customization import SavedCustomization
from entities.weapon import Weapon


@dataclass
class SavedWeapon:
    user_id: str
    id: str
    weapon: Weapon
    customizations: list[SavedCustomization] = field(default_factory=list)
