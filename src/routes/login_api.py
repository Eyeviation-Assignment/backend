import logging
from typing import Optional
from uuid import uuid4

from flask import Blueprint, request
from flask_login import current_user, login_user

from DTOs.login_dto import LoginDTO
from database.models.users_model import UsersModel
from database.shared_db import db
from exceptions.forbidden_exception import ForbiddenException

login_bp = Blueprint('login_api', __name__)


@login_bp.route('/login', methods=['POST'])
def login():
    login_dto = LoginDTO.from_dict(request.get_json())
    user_id: Optional[str] = None
    if current_user.is_authenticated:
        logging.info('user is authenticated')
        if login_dto.username != current_user.get_id():
            raise ForbiddenException('The server understood the request, but will not fulfill it, if it was correct.')
        user_id = current_user.get_id()
    else:
        user_model: UsersModel = _verify_login(login_dto.username)
        if not user_model:
            user_model = _create_new_user(login_dto.username)
        login_user(user_model)
        user_id = user_model.id
    if not user_id:
        raise ForbiddenException("Couldn't get user_id")
    return LoginDTO(username=login_dto.username).to_json()


def _verify_login(username: str) -> UsersModel:
    """
    This should be in a db methods but no time
    """
    user_model: UsersModel = (db.session.query(UsersModel)
                              .filter(UsersModel.username == username)
                              .first())
    return user_model


def _create_new_user(username: str) -> UsersModel:
    model = UsersModel(id=str(uuid4()), username=username)
    db.session.add(model)
    db.session.commit()
    return model
