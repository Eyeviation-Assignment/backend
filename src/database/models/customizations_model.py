from database.shared_db import db
from entities.customization import Customization
from enums.cutomizations_enum import CustomizationTypesEnum


class CustomizationsModel(db.Model):
    __tablename__ = 'customizations'
    id = db.Column(db.String(36), primary_key=True)
    customization_type = db.Column(db.String(255), nullable=False)
    customization_model = db.Column(db.String(255), nullable=False)

    db.UniqueConstraint('customization_type', 'customization_model', name='unique_customization_type_per_model'),

    weapons_to_customizations_model = db.relationship('WeaponsToCustomizationsModel', back_populates='customization_model')
    saved_customization_model = db.relationship('SavedCustomizationsModel', back_populates='customization_model')

    # Relationship to Weapon (optional, allows easy access to associated weapon)
    # weapon = db.relationship('Weapon', backref=db.backref('customizations', lazy=True))

    def convert_to_entity(self) -> Customization:
        return Customization(
            id=self.id,
            customization_model=self.customization_model,
            customization_type=CustomizationTypesEnum(self.customization_type)
        )
