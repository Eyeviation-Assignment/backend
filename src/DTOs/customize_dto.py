from dataclasses import dataclass
from typing import Optional

from dataclasses_json import DataClassJsonMixin

from enums.cutomizations_enum import CustomizationTypesEnum
from enums.sights_enum import SightsEnum
from enums.weapons_enum import WeaponsEnum


@dataclass
class CustomizationDTO(DataClassJsonMixin):
    id: str
    customization_type: CustomizationTypesEnum
    customization_model: str
