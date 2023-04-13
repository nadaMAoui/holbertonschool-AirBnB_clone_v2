#!/usr/bin/python3
"""
web flask app init
@app.route(''/')
@app.route('/hbnb')
server run
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slaches=False)
def Hello_HBNB():
    '''view function'''
    return 'Hello HBNB!'

@app.route("/hbnb", strict_slaches=False)
def HBNB():
    '''view function' '''
    return 'HBNB'
    

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
