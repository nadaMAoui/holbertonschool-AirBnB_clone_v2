#!/usr/bin/python3
"""
This module is a simple Flask application that defines several routes:
Routes:
- The homepage ("/") displays the message "Hello HBNB!" when visited.
- The "/hbnb" page displays the message "HBNB" when visited.
- The "/c/<text>" page is a dynamic route that replaces underscores
with spaces in the <text> parameter.
- The "/python/<text>" page is a dynamic route that displays "Python"
followed by a custom text string. If no text string is provided,
the default message "is cool" is used.
- The "/number/<int:n>" page is a dynamic route that
displays the message "<n> is a number" when visited,
where <n> is a provided integer.
- /number_template/<n>: display a HTML page only if n is an integer
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """View function displays Hello HBNB!"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """View function displays HBNB"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """Dynamic function display 'C ',
    followed by the value of the text variable.
    """
    return "C {}".format(text.replace("_", " "))


@app.route("/python/", defaults={"text": "is cool"}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text):
    """Dynamic function displays Python followed by the value
    of the text variable.
    """
    return "Python {}".format(text.replace("_", " "))


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """View function displays n if it's only integer"""
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """Displays HTML page if n is int"""
    return render_template("5-number.html", number=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
