from http import HTTPStatus
from flask import Blueprint, Response

after_request_bp = Blueprint('after_request', __name__)


# todo: not working if passing None or not a json, we should handle it somehow
@after_request_bp.after_app_request
def after_request(response: Response):
    if response.get_data is None:
        response.status_code = HTTPStatus.NO_CONTENT.value
    response.headers.set("Content-Type", "application/json; charset=UTF-8")
    return response
