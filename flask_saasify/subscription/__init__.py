from flask import Blueprint

from . import models

subscription_bp = Blueprint(
    "subscription", __name__, template_folder="templates", static_folder="static"
)

from . import routes
