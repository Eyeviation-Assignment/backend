# from flask import Blueprint, request
# from flask_login import current_user
#
# from DTOs.customize_dto import CustomizeRequestDTO
# from entities.weapon import Weapon
#
# customize_bp = Blueprint('customize_bp', __name__)
#
#
# @customize_bp.route('/customize', methods=['POST'])
# def create_weapon():
#     user_id: str = current_user.get_id()
#     customize_dto = CustomizeRequestDTO.from_dict(request.get_json())
#     weapon = Weapon(model=customize_dto.weapon, sight=customize_dto.sight)
#     return TeacherDTO(id=teacher.id).to_json()
#
#
# @customize_bp.route('/customize/<weapon_id>', methods=['POST'])
# def create_weapon(weapon_id):
#     user_id: str = current_user.get_id()
#     customize_dto = CustomizeRequestDTO.from_dict(request.get_json())
#     weapon = Weapon(model=customize_dto.weapon, sight=customize_dto.sight)
#     return TeacherDTO(id=teacher.id).to_json()
#
#
# @customize_bp.route('/customize', methods=['GET'])
# def get_weapons():
#     user_id: str = current_user.get_id()
#     teacher: Teacher = TeachersDbMethods.get_teacher(user_id)
#     if not teacher:
#         raise NotFoundException("Teacher with this user id doesn't exist")
#     return TeacherDTO(id=teacher.id).to_json()
#
#
# @customize_bp.route('/customize/<weapon_id>', methods=['GET'])
# def get_weapon(weapon_id):
#     user_id: str = current_user.get_id()
#     teacher: Teacher = TeachersDbMethods.get_teacher(user_id)
#     if not teacher:
#         raise NotFoundException("Teacher with this user id doesn't exist")
#     return TeacherDTO(id=teacher.id).to_json()
