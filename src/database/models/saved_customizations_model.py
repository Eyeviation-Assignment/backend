from database.shared_db import db


class SavedCustomizationsModel(db.Model):
    __tablename__ = 'saved_customizations'

    id = db.Column(db.String(36), primary_key=True)
    user_id = db.Column(db.String(36), db.ForeignKey('users.id'), nullable=False)
    saved_weapon_id = db.Column(db.String(36), db.ForeignKey('saved_weapons.id'), nullable=False, index=True)
    customization_id = db.Column(db.String(36), db.ForeignKey('customizations.id'), nullable=False)
    slot_type = db.Column(db.Integer, nullable=False)

    db.UniqueConstraint('saved_weapon_id', 'slot_type', name='unique_slot_per_weapon'),
