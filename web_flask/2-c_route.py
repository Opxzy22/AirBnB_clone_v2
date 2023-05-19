#!/usr/bin/python3
""" This script starts a flask web application """
from flask import Flask


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def hello_hbnb():
    """ home route configuration """

    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb():
    """ hbnb route configuration """

    return "HBNB"


@app.route("/c/<text>")
def c_text(text):
    """ c route configuration """

    return f"C {text.replace('_', ' ')}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)