from flask import Blueprint

from . import models

auth_bp = Blueprint("saasify_auth", __name__, template_folder="templates")

from . import routes
