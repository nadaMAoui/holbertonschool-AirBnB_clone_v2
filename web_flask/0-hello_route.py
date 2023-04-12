#!/usr/bin/python3
'''
initialiation flask application instance
'''
from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def Hello_HBNB():
    return 'Hello HBNB!'


if __name__ == '__main__':
app.run(host='0.0.0.0')
