from typing import Optional
from uuid import uuid4

from flask_sqlalchemy.query import Query
from sqlalchemy.orm import joinedload

from database.models.saved_customizations_model import SavedCustomizationsModel
from database.models.saved_weapons_model import SavedWeaponsModel
from database.models.weapons_model import WeaponsModel
from database.shared_db import db
from entities.saved_weapon import SavedWeapon
from entities.weapon import Weapon


class SavedWeaponsDbMethods:

    @staticmethod
    def upsert_saved_weapon(user_id: str, weapon_id: str, *, existed_saved_weapon_id: Optional[str] = None) -> SavedWeapon:
        model = SavedWeaponsModel(id=existed_saved_weapon_id if existed_saved_weapon_id else str(uuid4()), user_id=user_id, weapon_id=weapon_id)
        db.session.merge(model)
        db.session.commit()
        return model.convert_to_entity()

    @staticmethod
    def get_saved_weapon_with_customizations(saved_weapon_id: str) -> SavedWeapon:
        saved_weapon_model = db.session.query(SavedWeaponsModel).options(
            joinedload(SavedWeaponsModel.weapon_model),
            joinedload(SavedWeaponsModel.saved_customization_models)
        ).filter_by(id=saved_weapon_id).first()
        return saved_weapon_model.convert_to_entity()

    # @staticmethod
    # def get_saved_weapons() -> list[Weapon]:
    #     query: Query = db.session.query(WeaponsModel)
    #     weapon_models: list[WeaponsModel] = query.all()
    #     return [model.convert_to_entity() for model in weapon_models]
