#!/usr/bin/python3
""" This script creates a flash application """
from flask import Flask, render_template
from models import storage


app = Flask(__name__)


@app.teardown_appcontext
def remove(exception):
    """ removes the current session """

    storage.close()


@app.route("/states_list", strict_slashes=False)
def states_list():
    """ returns all the states in DBstorage """

    states = storage.all("State")
    states_dict = {val.id: val.name for val in states.values()}

    return render_template("7-states_list.html", states=states_dict)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
