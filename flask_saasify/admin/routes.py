from . import admin_bp
from flask import render_template

from flask_saasify import db

from flask_saasify.analytics.models import Event

@admin_bp.route("/")
def dashboard():
    # calculate average response_time_ms
    avg_response_time = Event.query.with_entities(
        db.func.avg(Event.response_time_ms)
    ).scalar()

    return render_template('saasify_dashboard.html', avg_response_time=avg_response_time)
