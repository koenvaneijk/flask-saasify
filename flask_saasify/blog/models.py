from flask_saasify import db


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128))
    body = db.Column(db.Text)
    author = db.Column(db.String(80), db.ForeignKey("user.username"))
    created_at = db.Column(db.DateTime, default=db.func.now())
