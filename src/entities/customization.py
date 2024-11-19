from dataclasses import dataclass
from enums.cutomizations_enum import CustomizationTypesEnum


@dataclass
class Customization:
    customization_type: CustomizationTypesEnum
    customization_model: str
    id: str
