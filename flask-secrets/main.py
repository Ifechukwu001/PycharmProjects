from flask import Flask, render_template
# Bootstrap
from flask_bootstrap import Bootstrap
# Forms
from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, SubmitField, validators
from wtforms.validators import DataRequired


# Form Class
class LoginForm(FlaskForm):
    email = EmailField(label="Email", validators=[DataRequired(), validators.Email()])
    password = PasswordField(label="Password", validators=[DataRequired(), validators.Length(min=8)])
    submit = SubmitField(label="Log In")


# Instantiation
def create_app():
    apk = Flask(__name__)
    apk.secret_key = "secret"
    Bootstrap(apk)
    return apk


app = create_app()


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=["GET", "POST"])
def login():
    l_form = LoginForm()
    if l_form.validate_on_submit():
        mail = l_form.email.data
        password = l_form.password.data
        if mail == "admin@email.com" and password == "12345678":
            return render_template("success.html")
        else:
            return render_template("denied.html")
    return render_template("login.html", form=l_form)


if __name__ == '__main__':
    app.run(debug=True)