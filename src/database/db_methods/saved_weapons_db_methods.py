from typing import Optional
from uuid import uuid4

from flask_sqlalchemy.query import Query
from sqlalchemy.orm import joinedload

from database.models.saved_weapons_model import SavedWeaponsModel
from database.shared_db import db
from entities.saved_weapon import SavedWeapon


class SavedWeaponsDbMethods:

    @staticmethod
    def upsert_saved_weapon(user_id: str, weapon_id: str, *, existed_saved_weapon_id: Optional[str] = None) -> SavedWeapon:
        model = SavedWeaponsModel(id=existed_saved_weapon_id if existed_saved_weapon_id else str(uuid4()), user_id=user_id, weapon_id=weapon_id)
        db.session.merge(model)
        db.session.commit()
        return model.convert_to_entity()

    @staticmethod
    def get_saved_weapon_with_customizations(saved_weapon_id: str) -> Optional[SavedWeapon]:
        saved_weapon_model = db.session.query(SavedWeaponsModel).options(
            joinedload(SavedWeaponsModel.weapon_model),
            joinedload(SavedWeaponsModel.saved_customization_models)
        ).filter(SavedWeaponsModel.id == saved_weapon_id).first()
        return saved_weapon_model.convert_to_entity() if saved_weapon_model else None

    @staticmethod
    def get_saved_weapons(user_id: str) -> list[SavedWeapon]:
        # todo: no pagination (lack of time)
        query: Query = db.session.query(SavedWeaponsModel).filter(SavedWeaponsModel.user_id == user_id)
        saved_weapon_models: list[SavedWeaponsModel] = query.all()
        return [model.convert_to_entity() for model in saved_weapon_models]
