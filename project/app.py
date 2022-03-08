from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":

        # TODO: Load image and call pixelator.py on image, returning the pixelated image

        return render_template("index.html")

    else:

        # TODO

        return render_template("index.html", birthdays=birthdays)