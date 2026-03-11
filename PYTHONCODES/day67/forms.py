from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
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


class CommentForm(FlaskForm):
    text = TextAreaField(
        "Comment",
        validators=[
            DataRequired(message="Comment cannot be empty."),
            Length(min=1, max=500, message="Comment must be 1-500 characters long."),
        ],
    )
    submit = SubmitField("Post Comment")
