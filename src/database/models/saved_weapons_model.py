from database.shared_db import db


class SavedWeaponsModel(db.Model):
    __tablename__ = 'saved_weapons'

    id = db.Column(db.String(36), primary_key=True)
    user_id = db.Column(db.String(36), db.ForeignKey('users.id'), nullable=False, index=True)
    weapon_id = db.Column(db.String(36), db.ForeignKey('weapons.id'), nullable=False)
