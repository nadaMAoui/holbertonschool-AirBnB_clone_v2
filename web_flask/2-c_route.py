#!/usr/bin/python3
"""
This module is a simple Flask application that displays three routes:
a homepage ("/"), an HBNB page ("/hbnb"),and a dynamic page ("/c/<text>")
that replaces underscores with spaces in the <text> parameter.
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def Hello_HBNB():
    """view function"""
    return 'Hello HBNB!'


@app.route("/hbnb", strict_slashes=False)
def HBNB():
    """view function"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def C(text):
    """Dynamic function """
    return 'C {:s}'.format(text.replace('_', ' '))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

