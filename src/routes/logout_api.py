from flask import Blueprint
from flask_login import logout_user, login_required

logout_bp = Blueprint('logout_api', __name__)


@logout_bp.route('/logout', methods=['POST'])
@login_required
def logout():
    logout_user()
    return ''
