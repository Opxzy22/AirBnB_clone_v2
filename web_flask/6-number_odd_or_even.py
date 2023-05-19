#!/usr/bin/python3
""" This script starts a flask web application """
from flask import Flask, render_template


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


@app.route("/python")
@app.route("/python/<text>")
def python_text(text="is_cool"):
    """ python route configuration """

    return f"Python {text.replace('_', ' ')}"


@app.route("/number/<int:n>")
def number(n):
    """ number route configuration """

    return f"{n} is a number"


@app.route("/number_template/<int:n>")
def number_template(n):
    """ number template route configuration """

    return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even/<int:n>")
def number_odd_or_even(n):
    """ number odd or even route configuration """

    if n % 2 == 0:
        val = "even"
    else:
        val = "odd"

    return render_template("6-number_odd_or_even.html", n=n, val=val)


app.run(host="0.0.0.0")
