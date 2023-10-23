#!/usr/bin/python3
"""start a flask web apllication
that listen to 0.0.0.0 on port 5000
"""
from flask import Flask
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def cleanup(self):
    storage.close()


@app.route("/states_list", strict_slashes=False)
def list_of_state(states):
    return render_template('7-states_list.html', states=states)
