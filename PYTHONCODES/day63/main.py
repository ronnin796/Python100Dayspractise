from flask import Flask, render_template, redirect, url_for, flash
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, IntegerField
from wtforms.validators import DataRequired, URL, NumberRange
import csv
from pathlib import Path
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SECRET_KEY"] = "8BYkEfBA6O6donzWlSihBXox7C0sKR6b"
Bootstrap5(app)


app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://flaskuser:1234@localhost/flaskdb"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


class Book(db.Model):
    __tablename__ = "books"

    id = db.Column(db.Integer, primary_key=True)
    bookname = db.Column(db.String(150), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    rating = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"<Book {self.bookname} by {self.author}>"


class BookForm(FlaskForm):
    bookname = StringField("Book Name", validators=[DataRequired()])
    author = StringField("Author", validators=[DataRequired()])
    rating = IntegerField(
        "Rating (1-10)",
        validators=[
            DataRequired(),
            NumberRange(min=1, max=10, message="Rating must be between 1 and 10"),
        ],
    )
    submit = SubmitField("Add Book")


all_books = []


@app.route("/")
def home():
    books = Book.query.all()
    return render_template("index.html", books=books)


@app.route("/add_book", methods=["GET", "POST"])
def add_book():
    form = BookForm()
    if form.validate_on_submit():
        book_name = form.bookname.data
        author = form.author.data
        rating = form.rating.data

        book_data = {"Book": book_name, "author": author, "rating": rating}
        all_books.append(book_data)
        new_book = Book(bookname=book_name, author=author, rating=rating)
        db.session.add(new_book)
        db.session.commit()
        flash("Book added successfully!")
        return redirect(url_for("home"))

    return render_template("add.html", form=form)


if __name__ == "__main__":
    app.run(debug=True)
