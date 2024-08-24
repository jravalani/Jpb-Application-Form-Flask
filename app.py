import os

from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

app.config["SECRET_KEY"] = os.getenv("FLASK_PASSWORD")
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("FLASK_DATABASE_URI")
db = SQLAlchemy(app)


class Form(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    email = db.Column(db.String(80))
    date = db.Column(db.Date)
    occupation = db.Column(db.String(80))


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        first_name = request.form["fname"]
        last_name = request.form["lname"]
        email = request.form["email"]
        _date = request.form["date"]
        occupation = request.form["occupation"]

        print(first_name, last_name, email, _date, occupation)

        # storing data into database
        form = Form(first_name=first_name, last_name=last_name, email=email, date=_date, occupation=occupation)
        db.session.add(form)
        db.session.commit()
    return render_template("index.html")


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        app.run(debug=True, port=5001)