from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from flask_login import LoginManager
from flask import flash, redirect, url_for
from flask_ckeditor import CKEditor


class Base(DeclarativeBase):
    pass


ckeditor = CKEditor()
login_manager = LoginManager()


db = SQLAlchemy(model_class=Base)


@login_manager.unauthorized_handler
def unauthorized_callback():
    flash("You must be logged in to access this page.", "warning")
    # Redirect to login page (or anywhere safe)
    return redirect(url_for("user.login"))
