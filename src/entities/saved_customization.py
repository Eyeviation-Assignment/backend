from dataclasses import dataclass

from entities.customization import Customization


@dataclass
class SavedCustomization:
    user_id: str
    id: str
    saved_weapon_id: str
    customization: Customization
