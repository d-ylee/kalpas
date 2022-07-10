from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()


def create_app(test_config=None):
    """
    Creates main app
    """
    from .config import Config

    app = Flask(__name__)
    app.config.from_object(Config)
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
    print(test_config)

    db.init_app(app)
    migrate.init_app(app, db)

    from . import users
    app.register_blueprint(users.bp)

    from . import timecard
    app.register_blueprint(timecard.bp)

    return app
