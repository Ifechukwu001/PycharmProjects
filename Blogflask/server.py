from flask import Flask, render_template
import datetime as dt
import requests

app = Flask(__name__)


# @app.route("/")
# def home():
#     name = "Ogidi Ifechukwu"
#     year = str(dt.datetime.now())[:4]
#     return render_template("index.html", yr=year, nm=name)


@app.route("/guess/<name>")
def guess(name):
    response_age = requests.get(f"http://api.agify.io?name={name}").json()["age"]
    response_gender = requests.get(f"https://api.genderize.io?name={name}").json()["gender"]
    return render_template("index.html", name=name, age=response_age, gender=response_gender)


if __name__ == "__main__":
    app.run(debug=True)
