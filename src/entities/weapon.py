from dataclasses import dataclass
from enums.weapons_enum import WeaponsEnum


@dataclass
class Weapon:
    model: WeaponsEnum
    id: str

# @dataclass
# class Weapon:
#     model: WeaponsEnum
#     sight: Optional[SightsEnum] = None
#     id: Optional[str] = None
#
#     def __post_init__(self):
#         self._validate_customization()
#
#     def _validate_customization(self):
#         if self.sight and not WeaponCustomizeValidatorUtils.is_valid_customization(self.model, self.sight):
#             raise InvalidCustomizationError(f'Invalid sight customization. sight: {self.sight.value}')
