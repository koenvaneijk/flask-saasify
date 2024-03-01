from datetime import datetime

from flask import Blueprint, g, request, session
from flask_login import current_user

from flask_saasify import db

from .models import Event

analytics_bp = Blueprint("saasify_analytics", __name__)


@analytics_bp.before_app_request
def before_request():
    g.request_start_time = datetime.utcnow()
    g.event = Event(
        user_id=current_user.id if current_user.is_authenticated else None,
        session_id=request.cookies.get(
            "session_id", None
        ),  # Assuming session ID is stored in cookies
        path=request.path,
        method=request.method,
        ip_address=request.remote_addr,
        user_agent=request.user_agent.string,
        referrer=request.referrer,
    )


@analytics_bp.after_app_request
def after_request(response):
    handling_time_ms = (datetime.utcnow() - g.request_start_time).total_seconds() * 1000
    g.event.status_code = response.status_code
    g.event.response_time_ms = handling_time_ms
    db.session.add(g.event)
    db.session.commit()
    return response
