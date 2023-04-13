#!/usr/bin/python3
"""
This module is a simple Flask application that defines several routes:
Routes:
- The homepage ("/") displays the message "Hello HBNB!" when visited.
- The "/hbnb" page displays the message "HBNB" when visited.
- The "/c/<text>" page is a dynamic route that replaces underscores with spaces in the <text> parameter.
- The "/python/<text>" page is a dynamic route that displays "Python"
followed by a custom text string. If no text string is provided, the default message "is cool" is used.
- The "/number/<int:n>" page is a dynamic route that
displays the message "<n> is a number" when visited, where <n> is a provided integer.

"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def Hello_HBNB():
    """Displays 'Hello HBNB!'"""
    return 'Hello HBNB!'
    

@app.route("/hbnb", strict_slashes=False)
def HBNB():
    """Displays 'HBNB'"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def C(text):
    """Displays 'C'"""
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)       
@app.route("/python/<text>", strict_slashes=False)
def python(text):
    """Displays 'Python'"""
    return 'Python {}'.format(text.replace('_', ' '))
       
@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """Displays a number"""
    return "{} is a number".format(n)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
