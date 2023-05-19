#!/usr/bin/python3
""" Starts up a web application server """
from flask import Flask, render_template
from models import storage


app = Flask(__name__)


@app.teardown_appcontext
def remove(exception):
    """ removes the current session """

    storage.close()


@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states():
    """ Gets the cities and states """

    states = storage.all("State")
    states_arr = []
    for state in states.values():
        state_dict = {}
        state_dict["id"] = state.id
        state_dict["name"] = state.name
        state_cities = state.cities
        state_dict["cities"] = state_cities
        states_arr.append(state_dict)

    return render_template("8-cities_by_states.html", states=states_arr)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
