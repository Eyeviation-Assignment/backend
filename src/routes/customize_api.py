from flask import Blueprint, request
from flask_login import current_user, login_required

from DTOs.customization_api_dto import CustomizationRequestDTO, CustomizationResponseDTO, SavedWeaponsAllResponseDTO, SavedWeaponDTO
from DTOs.customize_dto import CustomizationDTO
from DTOs.weapons_dto import WeaponDTO
from database.db_methods.saved_customizations_db_methods import SavedCustomizationsDbMethods
from database.db_methods.saved_weapons_db_methods import SavedWeaponsDbMethods
from entities.saved_customization import SavedCustomization
from entities.saved_weapon import SavedWeapon

customize_bp = Blueprint('customize_bp', __name__)


@customize_bp.route('/customize', methods=['POST'])
@login_required
def create_weapon():
    user_id: str = current_user.get_id()
    customize_dto = CustomizationRequestDTO.from_dict(request.get_json())
    saved_weapon: SavedWeapon = SavedWeaponsDbMethods.upsert_saved_weapon(user_id,
                                                                          customize_dto.weapon_id,
                                                                          existed_saved_weapon_id=customize_dto.saved_weapon_id)
    saved_customizations: list[SavedCustomization] = SavedCustomizationsDbMethods.upsert_saved_customization(user_id,
                                                                                                             saved_weapon.id,
                                                                                                             customize_dto.saved_customizations)
    saved_weapon = SavedWeaponsDbMethods.get_saved_weapon_with_customizations(saved_weapon.id)
    return CustomizationResponseDTO(
        saved_weapon_id=saved_weapon.id,
        saved_weapon=WeaponDTO(id=saved_weapon.weapon.id, model=saved_weapon.weapon.model),
        saved_customizations=[CustomizationDTO(id=saved_custom.id,
                                               customization_type=saved_custom.customization.customization_type,
                                               customization_model=saved_custom.customization.customization_model) for saved_custom in
                              saved_weapon.customizations]
    ).to_json()


@customize_bp.route('/customize', methods=['GET'])
def get_weapons():
    user_id: str = current_user.get_id()
    saved_weapons: list[SavedWeapon] = SavedWeaponsDbMethods.get_saved_weapons(user_id)
    return SavedWeaponsAllResponseDTO(weapons=[SavedWeaponDTO(id=saved_weapon.id,
                                                              weapon=WeaponDTO(id=saved_weapon.weapon.id, model=saved_weapon.weapon.model)) for
                                               saved_weapon in saved_weapons]).to_json()
#
#
# @customize_bp.route('/customize/<saved_weapon_id>', methods=['GET'])
# def get_weapon(saved_weapon_id):
#     user_id: str = current_user.get_id()
#     teacher: Teacher = TeachersDbMethods.get_teacher(user_id)
#     if not teacher:
#         raise NotFoundException("Teacher with this user id doesn't exist")
#     return TeacherDTO(id=teacher.id).to_json()
