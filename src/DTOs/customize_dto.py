from dataclasses import dataclass
from dataclasses_json import DataClassJsonMixin

from enums.cutomizations_enum import CustomizationTypesEnum


@dataclass
class CustomizationDTO(DataClassJsonMixin):
    id: str
    customization_type: CustomizationTypesEnum
    customization_model: str
