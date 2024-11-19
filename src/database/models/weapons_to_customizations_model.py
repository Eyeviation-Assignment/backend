from database.shared_db import db

# todo: important for cycling
from database.models.customizations_model import CustomizationsModel
from database.models.weapons_model import WeaponsModel


class WeaponsToCustomizationsModel(db.Model):
    __tablename__ = 'weapons_to_customizations'

    weapon_id = db.Column(db.String(36), db.ForeignKey('weapons.id'), nullable=False, primary_key=True)
    customization_id = db.Column(db.String(36), db.ForeignKey('customizations.id'), nullable=False, primary_key=True)

    weapon_model = db.relationship('WeaponsModel', back_populates='weapons_to_customizations_model')
    customization_model = db.relationship('CustomizationsModel', back_populates='weapons_to_customizations_model')
