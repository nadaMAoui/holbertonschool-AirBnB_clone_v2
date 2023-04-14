#!/usr/bin/python3
"""flask web application
"""
from flask import Flask, render_template
from os import environ
from models import storage
from models.state import State

app = Flask(__name__)
environ['FLASK_ENV'] = 'development'


@app.teardown_appcontext
def states_list_teardown(self):
    """ Ensures SQLAlchemy session opened to serve dynamic content for HTML
    templates is closed after serving.
    """
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    """ Requests list of `State`s ordered by name, which populates HTML
    template served to '/states_list'.
    """
    return render_template('7-states_list.html', states=storage.all(State))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')