from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        first_name = request.form["fname"]
        last_name = request.form["lname"]
        email = request.form["email"]
        _date = request.form["date"]
        occupation = request.form["occupation"]

        print(first_name, last_name, email, _date, occupation)
    return render_template("index.html")


app.run(debug=True, port=5001)