from flask.sansio.app import App

from utils.argon2_utils import ArgonUtils


def set_app_configs(app: App):
    app.config['SECRET_KEY'] = ArgonUtils.generate_secret_key()
    app.config.update(
        SESSION_COOKIE_SECURE=True,
        SESSION_COOKIE_HTTPONLY=True,
        SESSION_COOKIE_SAMESITE='None',
    )
