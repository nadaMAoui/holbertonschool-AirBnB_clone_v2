#!/usr/bin/python3
''' Flask web application that displays
a list of states from a database '''

from flask import Flask, render_template
from models.state import State
from models import storage

app = Flask(__name__)

@app.route('/states_list', strict_slashes=False)
def state_list():
    ''' Flask view function'''
    all_states = storage.all(State)
    return render_template('7-states_list.html', states=all_states)

@app.teardown_appcontext
def teardown_appcontext(self):
    ''' Function '''
    return storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
