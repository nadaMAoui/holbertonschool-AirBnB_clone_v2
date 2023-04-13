#!/usr/bin/python3
"""
This module is a simple Flask application
that displays three routes: a homepage ("/") and an HBNB page ("/hbnb")
and a text ("/c/<text>")
"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def Hello_HBNB():
    """view function"""
    return 'Hello HBNB!'
    

@app.route("/hbnb", strict_slaches=False)
def HBNB():
    """view function"""
    return "HBNB"


@app.route("/c/<text>", strict_slaches=False)
def C():
    """Dynamic function"""
    return  'C {:s}'.format(text.replace('_', ' '))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)    