from flask import Blueprint

from DTOs.customize_dto import CustomizationDTO
from DTOs.weapons_dto import WeaponDTO, WeaponsResponseDTO, WeaponWithCustomizationsResponseDTO
from database.db_methods.weapons_db_methods import WeaponsDbMethods
from database.db_methods.weapons_to_customizations_db_methods import WeaponsToCustomizationsDbMethods
from entities.weapon_with_customization import WeaponWithCustomization
from entities.weapon import Weapon
from enums.cutomizations_enum import CustomizationTypesEnum

weapon_bp = Blueprint('weapon_bp', __name__)


@weapon_bp.route('/weapons', methods=['GET'])
def get_weapons():
    weapons: list[Weapon] = WeaponsDbMethods.get_weapons()
    return WeaponsResponseDTO(weapons=[WeaponDTO(id=weapon.id, model=weapon.model) for weapon in weapons]).to_json()


@weapon_bp.route('/weapons/<weapon_id>', methods=['GET'])
def get_weapon_with_parts(weapon_id):
    weapon_with_customization: WeaponWithCustomization = WeaponsToCustomizationsDbMethods.get_weapon_with_customization(weapon_id)
    if not weapon_with_customization:
        raise Exception(f'No records')  # todo: no time but should be a specific error 404
    return _convert_to_weapon_with_customizations_dto(weapon_with_customization)


def _convert_to_weapon_with_customizations_dto(weapon_with_customization: WeaponWithCustomization) -> str:
    # todo: this is ugly but not time so we move on :D :X
    dto_dict: dict[CustomizationTypesEnum, list[CustomizationDTO]] = {}
    for key, list_of_customs in weapon_with_customization.customizations.items():
        if key not in dto_dict:
            dto_dict[key] = []
        for single_custom in list_of_customs:
            dto_dict[key].append(CustomizationDTO(id=single_custom.id,
                                                  customization_type=single_custom.customization_type,
                                                  customization_model=single_custom.customization_model))

    return WeaponWithCustomizationsResponseDTO(
        weapon=WeaponDTO(id=weapon_with_customization.weapon.id, model=weapon_with_customization.weapon.model),
        customizations=dto_dict
    ).to_json()
