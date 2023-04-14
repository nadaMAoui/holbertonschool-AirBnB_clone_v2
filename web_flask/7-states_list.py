#!/usr/bin/python3
'''Flask web application that displays
a list of states from a database'''

from flask import Flask, render_template
from models.state import State
from models import storage


app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def state_list():
    '''Flask view function that retrieves
    all states from the database
    and passes them to the HTML template
    to generate an HTML response'''
    all_states = storage.all(State)
    return render_template('7-states_list.html', states=all_states)


@app.teardown_appcontext
def teardown_appcontext(self):
    '''Function to close the database connection
    when the app context is torn down'''
    return storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
