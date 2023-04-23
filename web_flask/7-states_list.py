#!/usr/bin/python3
Update FileStorage: (models/engine/file_storage.py)

Add a public method def close(self):: call reload() method for deserializing the JSON file to objects
Update DBStorage: (models/engine/db_storage.py)

Add a public method def close(self):: call remove() method on the private session attribute (self.__session) tips or close() on the class Session tips
Update State: (models/state.py) - If it’s not already present

If your storage engine is not DBStorage, add a public getter method cities to return the list of City objects from storage linked to the current State
"""
from models import storage
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states_list():
    """Displays an HTML page with a list of all State objects in DBStorage.

    States are sorted by name.
    """
    states = storage.all("State")
    return render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def teardown(exc):
    """Remove the current SQLAlchemy session."""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
