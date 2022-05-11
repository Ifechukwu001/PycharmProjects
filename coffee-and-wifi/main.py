from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.fields.html5 import URLField
from wtforms.validators import DataRequired, URL
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


class CafeForm(FlaskForm):
    cafe_name = StringField("Cafe Name", validators=[DataRequired()])
    cafe_location = URLField("Cafe Location on Google Maps (URL)", validators=[URL()])
    open_time = StringField("Opening Time e.g 8AM", validators=[DataRequired()])
    close_time = StringField("Closing Time e.g 5:30PM", validators=[DataRequired()])
    coffee_rating = SelectField("Coffee Rating", choices=["☕", "☕☕", "☕☕☕", "☕☕☕☕", "☕☕☕☕☕"])
    wifi_rating = SelectField("Wifi Strenght Rating", choices=["❌", "💪", "💪💪", "💪💪💪", "💪💪💪💪", "💪💪💪💪💪"])
    power_available = SelectField("Power Socket Availability", choices=["❌", "🔌", "🔌🔌", "🔌🔌🔌", "🔌🔌🔌🔌", "🔌🔌🔌🔌🔌"])
    submit = SubmitField("Submit")

# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
# e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        print("True")
        # Exercise:
        # Make the form write a new row into cafe-data.csv
        # with   if form.validate_on_submit()
        data = [form.cafe_name.data, form.cafe_location.data, form.open_time.data, form.close_time.data,
                form.coffee_rating.data, form.wifi_rating.data, form.power_available.data]
        with open("cafe-data.csv", mode="a", encoding="utf8", newline="") as saved_data:
            cafe_data_writer = csv.writer(saved_data, delimiter=",")
            cafe_data_writer.writerow(data)

    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', encoding="utf8") as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
