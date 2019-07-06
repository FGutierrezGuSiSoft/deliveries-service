from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from project.configs import Config
from flask_cors import CORS


db = SQLAlchemy()
migrate = Migrate()


def register_blueprints(app):
    from project.views import blueprint

    app.register_blueprint(blueprint)


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    CORS(app)

    db.init_app(app)
    migrate.init_app(app, db)

    register_blueprints(app)

    @app.shell_context_processor
    def ctx():
        return {'app': app, 'db': db}

    return app
