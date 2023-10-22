#!/usr/bin/python3
""" Import Flask module from flask
python script that start web application
it listens on 0.0.0.0 to port 5000
"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ Returns some string to the page """
    return 'Hello HBNB!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
