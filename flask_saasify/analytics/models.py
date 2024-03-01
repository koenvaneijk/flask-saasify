from flask_saasify import db


class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(128), nullable=True)  # User identifier, if available
    session_id = db.Column(
        db.String(128), nullable=True
    )  # To track anonymous users or user sessions
    path = db.Column(db.String(255), nullable=False)  # Requested path
    method = db.Column(db.String(10), nullable=False)  # HTTP method (GET, POST, etc.)
    status_code = db.Column(db.Integer, nullable=True)  # Response status code
    response_time_ms = db.Column(
        db.Float, nullable=True
    )  # Response time in milliseconds
    timestamp = db.Column(db.DateTime, default=db.func.now())  # Timestamp of the event
    ip_address = db.Column(db.String(45), nullable=True)  # IP address of the requester
    user_agent = db.Column(
        db.Text, nullable=True
    )  # User agent of the requester's browser/device
    referrer = db.Column(db.Text, nullable=True)  # HTTP referrer

    def __repr__(self):
        return f"<Event {self.id} {self.path}>"
