#!/usr/bin/python3
""" This script starts a flask web application """
from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """ returns hello for a request to the / route """

    return "Hello HBNB!"


app.run(host="0.0.0.0")
