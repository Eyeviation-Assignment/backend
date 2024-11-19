from dataclasses import dataclass
from dataclasses_json import DataClassJsonMixin

from DTOs.customize_dto import CustomizationDTO
from enums.cutomizations_enum import CustomizationTypesEnum


@dataclass
class WeaponDTO(DataClassJsonMixin):
    id: str
    model: str


@dataclass
class WeaponsResponseDTO(DataClassJsonMixin):
    weapons: list[WeaponDTO]


@dataclass
class WeaponWithCustomizationsResponseDTO(DataClassJsonMixin):
    weapon: WeaponDTO
    customizations: dict[CustomizationTypesEnum, list[CustomizationDTO]]
