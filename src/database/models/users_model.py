from flask_login import UserMixin

from database.shared_db import db
from entities.user import User


class UsersModel(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.String(36), primary_key=True)
    username = db.Column(db.String(255), nullable=False)

    def convert_to_entity(self) -> User:
        return User(
            id=self.id,
            username=self.username
        )
