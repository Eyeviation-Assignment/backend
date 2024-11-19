import logging

from flask import Flask
from flask_cors import CORS
from flask_login import LoginManager

from after_request import after_request_bp
from app_config import set_app_configs
from database.models.users_model import UsersModel
from database.shared_db import db
from exceptions.exceptions_config import error_handler_bp
from routes.customize_api import customize_bp
from routes.login_api import login_bp
from routes.logout_api import logout_bp
from routes.weapons_api import weapon_bp

app = Flask(__name__)
login_manager = LoginManager(app)
app.register_blueprint(error_handler_bp)
app.register_blueprint(after_request_bp)
app.register_blueprint(weapon_bp)
app.register_blueprint(login_bp)
app.register_blueprint(logout_bp)
app.register_blueprint(customize_bp)
CORS(app, resources={r"/*": {"origins": 'http://localhost:3000'}}, supports_credentials=True)


@login_manager.user_loader
def load_user(user_id: str):
    return db.session.get(UsersModel, user_id)


@app.route('/')
def index():
    return 'Hello, World!'


def init_database() -> None:
    try:
        app.logger.info('Starting initializing database connection')
        host: str = '127.0.0.1'
        user: str = 'user'
        password: str = 'password'
        database: str = 'eyeviation'
        port: str = '3306'

        app.config[
            'SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{user}:{password}@{host}:{port}/{database}'
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

        db.init_app(app)
    except Exception as e:
        app.logger.error(f'Error while initializing database connection. Message:{str(e)}')


if __name__ == '__main__':
    logging.info('Starting server')
    init_database()
    set_app_configs(app)
    app.run(debug=True)
    