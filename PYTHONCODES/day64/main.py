from flask import Flask, render_template, redirect, url_for, request, flash
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, FloatField, TextAreaField
from wtforms.validators import DataRequired, NumberRange
import requests


# CREATE DB
app = Flask(__name__)
app.config["SECRET_KEY"] = "8BYkEfBA6O6donzWlSihBXox7C0sKR6b"
Bootstrap5(app)


app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://flaskuser:1234@localhost/flaskdb"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


class Movies(db.Model):
    __tablename__ = "movies"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    year = db.Column(db.String(150), nullable=False)
    review = db.Column(db.Text, nullable=True)
    description = db.Column(db.Text, nullable=True)
    rating = db.Column(db.Float, nullable=False)
    image_url = db.Column(db.String(300), nullable=True)

    def __repr__(self):
        return f"<Movie {self.title} by {self.rating}>"


class MovieForm(FlaskForm):
    title = StringField(
        "Title",
        validators=[DataRequired()],
        render_kw={"placeholder": "Enter movie title"},
    )
    year = StringField(
        "Year", validators=[DataRequired()], render_kw={"placeholder": "e.g., 2023"}
    )
    review = TextAreaField(
        "Review", render_kw={"placeholder": "Write your personal review here..."}
    )
    description = TextAreaField(
        "Description",
        render_kw={"placeholder": "Brief movie description or synopsis..."},
    )
    rating = FloatField(
        "Rating (0-10)",
        validators=[
            DataRequired(),
            NumberRange(min=0, max=10, message="Rating must be between 0 and 10"),
        ],
        render_kw={"placeholder": "Rate the movie (0-10)"},
    )
    image_url = StringField(
        "Image URL",
        render_kw={"placeholder": "Paste an image URL for the movie poster"},
    )
    submit = SubmitField("Add Movie")


@app.route("/")
def home():

    movies = Movies.query.order_by(Movies.rating.desc()).limit(10).all()
    for idx, movie in enumerate(movies, start=1):
        movie.position = idx
    return render_template("index.html", movies=movies)


@app.route("/add_movie", methods=["GET", "POST"])
def add_movie():
    form = MovieForm()
    if form.validate_on_submit():
        title = form.title.data
        year = form.year.data
        review = form.review.data
        description = form.description.data
        rating = form.rating.data
        image_url = form.image_url.data

        # Create new movie instance
        new_movie = Movies(
            title=title,
            year=year,
            review=review,
            description=description,
            rating=rating,
            image_url=image_url,
        )
        db.session.add(new_movie)
        db.session.commit()
        flash(f"Movie '{title}' added successfully!")
        return redirect(url_for("home"))

    return render_template("add.html", form=form)


@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit_movie(id):
    movie = Movies.query.get_or_404(id)
    form = MovieForm(obj=movie)  # populate form with current data

    if form.validate_on_submit():

        movie.title = form.title.data
        movie.year = form.year.data
        movie.review = form.review.data
        movie.description = form.description.data
        movie.rating = form.rating.data
        movie.image_url = form.image_url.data

        db.session.commit()
        flash(f"Movie '{movie.title}' updated successfully!")
        return redirect(url_for("home"))

    return render_template("edit.html", form=form, movie=movie)


@app.route("/delete/<int:id>", methods=["POST"])
def delete_movie(id):
    movie = Movies.query.get_or_404(id)  # fetch the movie
    db.session.delete(movie)  # delete from DB
    db.session.commit()  # commit changes
    flash(f"Movie '{movie.title}' deleted successfully!")
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)
