from flask_sqlalchemy.query import Query

from database.models.weapons_to_customizations_model import WeaponsToCustomizationsModel
from database.shared_db import db
from entities.customization import Customization
from entities.weapon_with_customization import WeaponWithCustomization
from enums.cutomizations_enum import CustomizationTypesEnum


class WeaponsToCustomizationsDbMethods:

    @staticmethod
    def get_weapon_with_customization(weapon_id: str) -> WeaponWithCustomization:
        query: Query = db.session.query(WeaponsToCustomizationsModel).filter_by(weapon_id=weapon_id)
        weapon_to_customization_models: list[WeaponsToCustomizationsModel] = query.all()
        if not weapon_to_customization_models:
            raise Exception(f'No records')  # todo: no time but should be a specific error
        return WeaponWithCustomization(weapon=weapon_to_customization_models[0].weapon_model.convert_to_entity(),
                                       customizations=WeaponsToCustomizationsDbMethods._type_to_customizations(weapon_to_customization_models))

    @staticmethod
    def _type_to_customizations(weapon_to_customization_models: list[WeaponsToCustomizationsModel]) -> dict[CustomizationTypesEnum, list[Customization]]:
        customizations_by_type: dict[CustomizationTypesEnum, list[Customization]] = {}

        for weapon_to_customization_model in weapon_to_customization_models:
            customization: Customization = weapon_to_customization_model.customization_model.convert_to_entity()
            if customization.customization_type not in customizations_by_type:
                customizations_by_type[customization.customization_type] = []
            customizations_by_type[customization.customization_type].append(customization)
        return customizations_by_type
