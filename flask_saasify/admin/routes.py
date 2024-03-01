from . import admin_bp


@admin_bp.route("/")
def index():
    return "Admin page"
