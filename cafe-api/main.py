import random
from flask import Flask, jsonify, redirect, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dic(self):
        # Method 1.
        dictionary = {}
        # Loop through each column in the data record
        for column in self.__table__.columns:
            # Create a new dictionary entry;
            # where the key is the name of the column
            # and the value is the value of the column
            dictionary[column.name] = getattr(self, column.name)
        return dictionary


@app.route("/")
def home():
    return redirect("https://documenter.getpostman.com/view/18989194/UVRHi3qi")


# HTTP GET - Read Record

@app.route("/random")
def get_random_cafe():
    cafes = db.session.query(Cafe).all()
    random_cafe = random.choice(cafes)
    return jsonify(cafe=random_cafe.to_dic())


@app.route("/all")
def all_cafes():
    cafes = db.session.query(Cafe).all()
    cafes_list = [cafe.to_dic() for cafe in cafes]
    return jsonify(all_cafes=cafes_list)


@app.route("/search")
def search():
    location = request.args.get("loc")
    cafe = db.session.query(Cafe).filter_by(location=location).first()
    if cafe:
        return jsonify(cafe=cafe.to_dic())
    else:
        return jsonify(error={
            "Not Found": "Sorry, we don't have a cafe at that location."
        }), 404


# HTTP POST - Create Record

@app.route("/add", methods=["POST"])
def add_cafe():
    name = request.form["name"]
    map_url = request.form["map_url"]
    img_url = request.form["img_url"]
    location = request.form["location"]
    seats = request.form["seats"]
    has_toilet = bool(request.form["has_toilet"])
    has_wifi = bool(request.form["has_wifi"])
    has_sockets = bool(request.form["has_sockets"])
    can_take_calls = bool(request.form["can_take_calls"])
    coffee_price = request.form["coffee_price"]

    new_cafe = Cafe(name=name,
                    map_url=map_url,
                    img_url=img_url,
                    location=location,
                    seats=seats,
                    has_toilet=has_toilet,
                    has_wifi=has_wifi,
                    has_sockets=has_sockets,
                    can_take_calls=can_take_calls,
                    coffee_price=coffee_price)
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"Success": "Successfully added the new cafe."})


# HTTP PUT/PATCH - Update Record

@app.route("/update-price/<cafe_id>", methods=["PATCH"])
def update_price(cafe_id):
    new_price = request.args.get("new_price")
    cafe = db.session.query(Cafe).get(cafe_id)
    if cafe:
        cafe.coffee_price = new_price
        db.session.commit()
        return jsonify(response={"Success": "Successfully updated the price."})
    else:
        return jsonify(error={"Not Found": "Sorry a cafe with that id was not found."}), 404


# HTTP DELETE - Delete Record

@app.route("/report-closed/<cafe_id>", methods=["DELETE"])
def delete_cafe(cafe_id):
    if request.args.get("api_key") == "TopSecretAPIKey":
        cafe_to_delete = db.session.query(Cafe).get(cafe_id)
        if cafe_to_delete:
            db.session.delete(cafe_to_delete)
            db.session.commit()
            return jsonify(response={"Success": "You have deleted the cafe."})
        else:
            return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404
    else:
        return jsonify(error="Sorry not allowed. Make sure you have the correct api_key."), 403




if __name__ == '__main__':
    app.run(debug=True)
