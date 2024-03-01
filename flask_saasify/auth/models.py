import os

from flask_login import UserMixin
from flask_saasify import db, login_manager

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String)
    secret_token = db.Column(db.String)
    secret_confirmation = db.Column(db.Integer)
    last_login_at = db.Column(db.String)

    @property
    def role(self):
        admins = os.environ.get("ADMINS").split(",")

        if self.email in admins:
            return "admin"
        else:
            return "user"

    def is_admin(self):
        return self.role == "admin"

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
