#!/usr/bin/python3
""" This module starts a web application server """
from flask import Flask, render_template
from models import storage


app = Flask(__name__)


@app.teardown_appcontext
def remove(exception):
    """ Removes the current session """

    storage.close()


@app.route("/states", strict_slashes=False)
def states():
    """ Configures the state route """

    states = storage.all("State")

    return render_template("9-states.html", states=states, route="states")


@app.route("/states/<id>", strict_slashes=False)
def states_id(id):
    """ Configures the routes for a particular state """

    states = storage.all()
    found_state = None
    cities = None
    for state in states.values():
        if state.id == id:
            found_state = state
            break

    if found_state:
        cities = found_state.cities

    return render_template("9-states.html",
                           state=found_state,
                           cities=cities,
                           route="state_id")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
