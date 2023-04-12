#!/usr/bin/python3
"""Starts a Flask web application.
The application listens on 0.0.0.0, port 5000.
Routes:
    /: Displays 'Hello HBNB!'
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


@app.route('/python/', defaults={'text': 'is cool'}, strict_slaches=False)       
@app.route("/python/<text>", strict_slaches=False)
def python():
    """Display 'python'"""
    return 'python {:s}', format(text.replace('_', ' '))
       
@app.route('/number/<int:n>', strict_slaches=False)
def number(n):
    """Display number"""
    return "{} is a number".format(n)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)