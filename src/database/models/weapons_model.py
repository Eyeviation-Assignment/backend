from database.shared_db import db
from entities.weapon import Weapon


class WeaponsModel(db.Model):
    __tablename__ = 'weapons'

    id = db.Column(db.String(36), primary_key=True)
    model = db.Column(db.String(255), nullable=False)

    weapons_to_customizations_model = db.relationship('WeaponsToCustomizationsModel', back_populates='weapon_model')

    def convert_to_entity(self) -> Weapon:
        return Weapon(
            id=self.id,
            model=self.model
        )
