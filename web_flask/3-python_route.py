#!/usr/bin/python3
"""
This module is a simple Flask application that displays three routes:
a homepage ("/"), an HBNB page ("/hbnb"),and a dynamic page ("/c/<text>")
that replaces underscores with spaces in the <text> parameter and a dynamic function
to display python with "text"
"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def Hello_HBNB():
    """Displays 'Hello HBNB!'"""
    return 'Hello HBNB!'
    

@app.route("/hbnb", strict_slaches=False)
def HBNB():
    """Display 'HBNB'"""
    return "HBNB"


@app.route("/c/<text>", strict_slaches=False)
def C():
    """Display 'C'"""
    return  'C {:s}'.format(text.replace('_', ' '))


@app.route("/python/<text>", strict_slaches=False)
@app.route("/python/<text>", strict_slaches=False)
def python(text = "is cool")
    """Display 'Python' """
    return 'python %s' %text.replace('_', ' ')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
