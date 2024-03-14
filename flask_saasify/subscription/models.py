import os

from flask_saasify import db


# Define your own PLAN dictionary


class Subscription(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    plan_id = db.Column(db.String(50), default="free")
    start_date = db.Column(db.DateTime, default=db.func.now())
    end_date = db.Column(db.DateTime)
    status = db.Column(db.String(20), default="active")

    user = db.relationship("User", back_populates="subscription")


class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subscription_id = db.Column(
        db.Integer, db.ForeignKey("subscription.id"), nullable=False
    )
    transaction_date = db.Column(db.DateTime, nullable=False)
    amount = db.Column(db.Numeric(10, 2), nullable=False)
    status = db.Column(db.String(20), nullable=False)
    # Other transaction fields...

    subscription = db.relationship(
        "Subscription", backref=db.backref("transactions", lazy=True)
    )
