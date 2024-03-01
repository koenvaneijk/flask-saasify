from flask import Blueprint, flash, redirect, url_for
from flask_login import current_user

admin_bp = Blueprint("saasify_admin", __name__, template_folder="templates")


@admin_bp.before_request
def check_admin_role():
    if not current_user.is_authenticated or current_user.role != "admin":
        flash("You must be an admin to access this page.", "danger")
        return redirect("/")


from . import routes
