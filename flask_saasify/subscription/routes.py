from flask import render_template, redirect, url_for
from flask_saasify import login_required

from . import subscription_bp


@subscription_bp.route("/")
@login_required
def index():
    return render_template("subscription_index.html")


@subscription_bp.route("/cancel")
@login_required
def cancel():
    # cancel subscription
    return redirect(url_for("subscription.index"))
