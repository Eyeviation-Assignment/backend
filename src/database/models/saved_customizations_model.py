from database.shared_db import db
from entities.saved_customization import SavedCustomization


class SavedCustomizationsModel(db.Model):
    __tablename__ = 'saved_customizations'

    id = db.Column(db.String(36), primary_key=True)
    user_id = db.Column(db.String(36), db.ForeignKey('users.id'), nullable=False)
    saved_weapon_id = db.Column(db.String(36), db.ForeignKey('saved_weapons.id'), nullable=False, index=True)
    customization_id = db.Column(db.String(36), db.ForeignKey('customizations.id'), nullable=False)
    slot_type = db.Column(db.String(255), nullable=False)

    db.UniqueConstraint('saved_weapon_id', 'slot_type', name='unique_slot_per_weapon'),
    customization_model = db.relationship('CustomizationsModel', back_populates='saved_customization_model')
    saved_weapon_model = db.relationship('SavedWeaponsModel', back_populates='saved_customization_models')

    def convert_to_entity(self) -> SavedCustomization:
        return SavedCustomization(
            id=self.id,
            user_id=self.user_id,
            saved_weapon_id=self.saved_weapon_id,
            customization=self.customization_model.convert_to_entity() if self.customization_model else None
        )
