from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests

MOVIE_SEARCH_API = "https://api.themoviedb.org/3/search/movie"
MOVIE_API = "https://api.themoviedb.org/3/movie/"
API_KEY = "cfec1d6c0362c0cd11ee0ac199ba11a9"

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movies-data.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
Bootstrap(app)
db = SQLAlchemy(app)


class AddMovie(FlaskForm):
    movie = StringField(label="Movie Title", validators=[DataRequired()])
    submit = SubmitField(label="Add Movie")


class RateMovieForm(FlaskForm):
    rating = StringField(label="Your rating out of 10 e.g 7.5", validators=[DataRequired()])
    review = StringField(label="Your Review", validators=[DataRequired()])
    submit = SubmitField(label="Done")


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(255), nullable=False)
    rating = db.Column(db.Float)
    ranking = db.Column(db.Integer, unique=True)
    review = db.Column(db.String(255))
    img_url = db.Column(db.String(255), unique=True, nullable=False)

    def __repr__(self):
        return f"Movie {Movie.title}"


db.create_all()


@app.route("/")
def home():
    movies = Movie.query.order_by(Movie.rating).all()

    # This line loops through all the movies
    for i in range(len(movies)):
        # This line gives each movie a new ranking reversed from their order in all_movies
        movies[i].ranking = len(movies) - i
    db.session.commit()
    return render_template("index.html", data_bank=movies)


@app.route("/edit", methods=["GET", "POST"])
def edit_rating():
    movie_id = request.args.get("id")
    movie = Movie.query.get(movie_id)
    rate_form = RateMovieForm()
    if rate_form.validate_on_submit():
        rate = float(request.form["rating"])
        review = request.form["review"]
        movie.rating = rate
        movie.review = review
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("edit.html", data=movie, form=rate_form)


@app.route("/delete")
def delete_movie():
    id = int(request.args.get("id"))
    movie_2_delete = Movie.query.get(id)
    db.session.delete(movie_2_delete)
    db.session.commit()
    return redirect(url_for("home"))


@app.route("/add", methods=["GET", "POST"])
def add_movie():
    movie = AddMovie()
    if movie.validate_on_submit():
        movie_title = request.form["movie"]
        params = {
            "api_key": API_KEY,
            "query": movie_title,
        }
        response_data = requests.get(url=MOVIE_SEARCH_API, params=params)
        search_query = response_data.json()["results"]
        return render_template("select.html", search=search_query)
    return render_template("add.html", form=movie)


@app.route("/movie/<id>")
def movie(id):
    params = {
        "api_key": API_KEY
    }
    response_data = requests.get(url=f"{MOVIE_API}{id}", params=params).json()
    title = response_data["title"]
    year = response_data["release_date"][:4]
    description = response_data["overview"]
    img_url = f"https://image.tmdb.org/t/p/original{response_data['poster_path']}"
    new_movie = Movie(title=title, year=year, description=description, img_url=img_url)
    db.session.add(new_movie)
    db.session.commit()
    return redirect(url_for("edit_rating", id=new_movie.id))


if __name__ == '__main__':
    app.run(debug=True)
