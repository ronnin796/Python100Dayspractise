from flask import Blueprint, render_template, redirect, url_for, flash, request, jsonify
from extensions import db, login_manager
from models import User
from forms import UserForm, LoginForm
from datetime import date
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import (
    UserMixin,
    login_user,
    LoginManager,
    login_required,
    current_user,
    logout_user,
)

user_bp = Blueprint("user", __name__)


@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User, int(user_id))


@user_bp.route("/register", methods=["GET", "POST"])
def register():
    form = UserForm()

    if form.validate_on_submit():
        if User.query.filter_by(email=form.email.data).first():
            flash("Email already registered. Please log in.", "danger")
            return redirect(url_for("user.register"))
        new_user = User(
            email=form.email.data,
            name=form.name.data,
            password=generate_password_hash(
                form.password.data, method="pbkdf2:sha256", salt_length=8
            ),
            is_admin=False,
        )

        db.session.add(new_user)
        db.session.commit()

        flash("Registration successful!", "success")
        login_user(new_user)
        return redirect(url_for("blog.get_all_posts"))

    return render_template("register.html", form=form)


@user_bp.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = db.session.execute(
            db.select(User).filter_by(email=form.email.data)
        ).scalar()
        if not user or not check_password_hash(user.password, form.password.data):
            flash("Wrong email or password", "danger")
            return redirect(url_for("user.login"))

        login_user(user)
        flash("Login successful", "success")
        return redirect(url_for("blog.get_all_posts"))

    return render_template("login.html", form=form)


@user_bp.route("/logout")
@login_required
def logout():
    logout_user()
    flash("You have been logged out.", "success")
    return redirect(url_for("blog.get_all_posts"))
