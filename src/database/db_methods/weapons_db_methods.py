from flask_sqlalchemy.query import Query

from database.models.weapons_model import WeaponsModel
from database.shared_db import db
from entities.weapon import Weapon


class WeaponsDbMethods:

    @staticmethod
    def get_weapons() -> list[Weapon]:
        query: Query = db.session.query(WeaponsModel)
        weapon_models: list[WeaponsModel] = query.all()
        return [model.convert_to_entity() for model in weapon_models]
