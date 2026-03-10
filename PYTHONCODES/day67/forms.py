from wtforms import StringField, PasswordField, BooleanField, SubmitField
from flask_ckeditor import CKEditor, CKEditorField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Email, Length, EqualTo, URL


class UserForm(FlaskForm):
    name = StringField(
        "Full Name", validators=[DataRequired(), Length(min=2, max=1000)]
    )

    email = StringField("Email", validators=[DataRequired(), Email(), Length(max=100)])

    password = PasswordField(
        "Password", validators=[DataRequired(), Length(min=6, max=100)]
    )

    confirm_password = PasswordField(
        "Confirm Password",
        validators=[
            DataRequired(),
            EqualTo("password", message="Passwords must match."),
        ],
    )

    is_admin = BooleanField("Admin Privileges")

    submit = SubmitField("Submit")


class BlogPostForm(FlaskForm):
    title = StringField("Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    author = StringField("Author Name", validators=[DataRequired()])
    img_url = StringField("Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")


class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email(), Length(max=100)])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=6)])
    submit = SubmitField("Login")
