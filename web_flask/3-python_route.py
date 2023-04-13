#!/usr/bin/python3
"""
This module is a simple Flask application that displays three routes:
a homepage ("/"), an HBNB page ("/hbnb"),
a dynamic page ("/c/<text>")
that replaces underscores with spaces in the
<text> parameter, and a dynamic function
to display "Python" followed by a custom text string.

"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def Hello_HBNB():
    """Displays 'Hello HBNB!'"""
    return 'Hello HBNB!'


@app.route("/hbnb", strict_slashes=False)
def HBNB():
    """Display 'HBNB'"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def C(text):
    """Displays 'C' """
    return 'C {:s}'.format(text.replace('_', ' '))


@app.route("/python/", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text="is cool"):
    """Displays 'Python' followed by the <text>
    """
    return 'Python {:s}' % text.replace('_', ' ')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
