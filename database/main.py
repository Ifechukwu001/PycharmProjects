import sqlite3
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# db = sqlite3.connect("books-collections.db")
#
# cursor = db.cursor()
#
# cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) "
#                "NOT NULL, rating FLOAT NOT NULL)")
#
# cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
# db.commit()


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///new-books-collection.db"
# Optional: But it will silence the deprecation warning in the console.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True, nullable=False)
    author = db.Column(db.String(80), unique=True)
    rating = db.Column(db.Float, nullable=False)

    # Optional: this will allow each book object to be identified by its title when printed.
    def __repr__(self):
        return f'<Book {self.title}>'


db.create_all()

new_book = Book(id=1, title="Harry Potter", author="J. K. Rowling", rating=9.3)

db.session.add(new_book)
db.session.commit()