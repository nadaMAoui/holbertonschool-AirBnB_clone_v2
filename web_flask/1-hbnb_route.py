#!/usr/bin/python3
"""
This module is a simple Flask application
that displays two routes: a homepage ("/") and an HBNB page ("/hbnb").
"""

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def Hello_HBNB():
    '''view function'''
    return 'Hello HBNB!'


@app.route("/hbnb", strict_slashes=False)
def HBNB():
    '''view function '''
    return 'HBNB'


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
