from flask import Blueprint
from flask_login import current_user, login_required
auth_bp = Blueprint('auth_api', __name__)


@auth_bp.route('/auth', methods=['GET'])
@login_required
def is_authenticate():
    user_id: str = current_user.get_id()
    return {'user_id': user_id}
