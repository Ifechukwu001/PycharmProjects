from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home_page():
    return render_template("index.html")


@app.route('/login', methods=['POST'])
def login():
    if request.method == "POST":
        user = request.form["username"]
        passwd = request.form["password"]
    return f"Name: {user}, Password: {passwd}"


if __name__ == "__main__":
    app.run(debug=True)