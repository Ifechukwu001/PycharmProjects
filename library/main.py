from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import FloatField, SubmitField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///book-collection.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = "kjbuyioh9ubfiurg55465453jhbgytgsbfuhbv"
db = SQLAlchemy(app=app)


class RateForm(FlaskForm):
    rate = FloatField(label="", validators=[DataRequired()], render_kw={"placeholder": "New Rating"})
    submit = SubmitField("Change Rating")


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Book {self.title}>'


db.create_all()

@app.route('/')
def home():
    books = Book.query.order_by(Book.title).all()
    return render_template("index.html", books=books)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        book_name = request.form["book-name"]
        book_author = request.form["book-author"]
        rating = request.form["rating"]
        new_book = Book(title=book_name, author=book_author, rating=rating)
        db.session.add(new_book)
        db.session.commit()
    return render_template("add.html")


@app.route("/edit/id=<id>", methods=["POST", "GET"])
def rating(id):
    book_id = id
    book = Book.query.filter_by(id=book_id).first()
    book_data = {
        "title": book.title,
        "rating": book.rating,
    }
    r_form = RateForm()
    if request.method == "POST":
        book.rating = request.form["rate"].data
    return render_template("rating.html", form=r_form, data=book_data)


if __name__ == "__main__":
    app.run(debug=True)

