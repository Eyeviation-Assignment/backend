from dataclasses import dataclass
from typing import Optional

from dataclasses_json import DataClassJsonMixin

from DTOs.customize_dto import CustomizationDTO
from DTOs.weapons_dto import WeaponDTO
from enums.cutomizations_enum import CustomizationTypesEnum


@dataclass
class SavedCustomizationDTO(DataClassJsonMixin):
    id: str
    slot: CustomizationTypesEnum


@dataclass
class CustomizationRequestDTO(DataClassJsonMixin):
    saved_customizations: list[SavedCustomizationDTO]
    weapon_id: str
    saved_weapon_id: Optional[str] = None


@dataclass
class CustomizationResponseDTO(DataClassJsonMixin):
    saved_weapon_id: str
    saved_customizations: list[CustomizationDTO]
    saved_weapon: WeaponDTO


@dataclass
class SavedWeaponDTO(DataClassJsonMixin):
    id: str
    weapon: WeaponDTO


@dataclass
class SavedWeaponsAllResponseDTO(DataClassJsonMixin):
    weapons: list[SavedWeaponDTO]
