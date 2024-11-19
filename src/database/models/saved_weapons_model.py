from database.shared_db import db
from entities.saved_weapon import SavedWeapon


class SavedWeaponsModel(db.Model):
    __tablename__ = 'saved_weapons'

    id = db.Column(db.String(36), primary_key=True)
    user_id = db.Column(db.String(36), db.ForeignKey('users.id'), nullable=False, index=True)
    weapon_id = db.Column(db.String(36), db.ForeignKey('weapons.id'), nullable=False)

    weapon_model = db.relationship('WeaponsModel', back_populates='saved_weapon_model')
    saved_customization_models = db.relationship('SavedCustomizationsModel', back_populates='saved_weapon_model')

    def convert_to_entity(self) -> SavedWeapon:
        return SavedWeapon(
            id=self.id,
            user_id=self.user_id,
            weapon=self.weapon_model.convert_to_entity() if self.weapon_model else None,
            customizations=[saved_custom_model.convert_to_entity() for saved_custom_model in self.saved_customization_models]
        )
