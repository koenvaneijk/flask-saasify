import os

from dotenv import load_dotenv
from flask_login import LoginManager, login_required, current_user
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()


class Saasify:
    def __init__(self, app=None):
        self.app = app

        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        load_dotenv()

        app.config["SECRET_KEY"] = os.environ["SECRET_KEY"]
        app.config["SQLALCHEMY_DATABASE_URI"] = os.environ["DATABASE_URI"]

        db.init_app(app)
        migrate.init_app(app, db)
        login_manager.init_app(app)
        login_manager.login_view = "saasify_auth.sign_in"

        from flask_saasify.analytics import analytics_bp

        app.register_blueprint(analytics_bp)

        from flask_saasify.auth import auth_bp

        app.register_blueprint(auth_bp, url_prefix="/auth")

        from flask_saasify.blog import blog_bp

        app.register_blueprint(blog_bp)

        from flask_saasify.core import core_bp

        app.register_blueprint(core_bp)

        from flask_saasify.admin import admin_bp

        app.register_blueprint(admin_bp, url_prefix="/admin")

        with app.app_context():
            db.create_all()

        return app
