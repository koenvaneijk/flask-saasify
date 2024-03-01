import os
import secrets
from urllib.parse import quote, urljoin, urlparse

from flask import flash, redirect, render_template, request
from flask_login import login_required, login_user, logout_user

from flask_saasify import db

from . import auth_bp
from .forms import LoginForm
from .models import User


def is_safe_url(target):
    ref_url = urlparse(request.host_url)
    test_url = urlparse(urljoin(request.host_url, target))
    return test_url.scheme in ("http", "https") and ref_url.netloc == test_url.netloc


@auth_bp.route("/", methods=["GET", "POST"])
def sign_in():
    next_url = request.args.get("next", "/")

    if request.method == "GET":
        token = request.args.get("token")

        if token:
            user = User.query.filter_by(secret_token=token).first()
            if user:
                login_user(user)
                user.secret_token = None
                db.session.commit()
                flash("Succesfully signed in.", category="success")

                if next and is_safe_url(next):
                    return redirect(next)
                else:
                    return redirect("/")
            else:
                flash(
                    "Oops! The link you used is invalid or expired. Please try logging in again.",
                    category="danger",
                )

    form = LoginForm()

    if form.validate_on_submit():
        # log in user
        user = User.query.filter_by(email=form.email.data.lower()).first()

        if not user:
            user = User(email=form.email.data.lower())
            db.session.add(user)
            db.session.commit()

            print(
                user.email,
                "Thank you for signing up! 👏",
                "emails/thank_you.html",
                {"message": "Thank you for signing up for AppEase!"},
            )  # TODO: Send email

            flash("Thank you for signing up! 👏")

        user.secret_token = secrets.token_urlsafe(32)
        db.session.commit()

        # Send link
        encoded_next_url = quote(next_url)
        base_url = os.environ["EXTERNAL_BASE_URL"]
        url = f"{base_url}/auth?token={user.secret_token}&next={encoded_next_url}"

        print(
            user.email,
            "Your magic link! 🪄",
            "emails/magic_link.html",
            {"url": url},
        )  # TODO: Send email
        flash(f"Magic link sent to {user.email}! 🪄")

        return render_template("check_mail.html")
    return render_template("sign_in.html", form=form)


@auth_bp.route("/logout")
@login_required
def sign_out():
    logout_user()
    return redirect("/")
