#!/usr/bin/python3
"""
fask web application instance
"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def Hello_HBNB():
    """view function'"""
    return 'Hello HBNB!'


if __name__ == '__main__':
app.run(host='0.0.0.0')
