#!/usr/bin/python3
""" Starts a Flash Web Application """
from models import storage
from models.catagory import Catagory
from flask import Flask, render_template
app = Flask(__name__)
# app.jinja_env.trim_blocks = True
# app.jinja_env.lstrip_blocks = True


@app.teardown_appcontext
def close_db(error):
    """ Remove the current SQLAlchemy Session """
    storage.close()


@app.route('/catagories_list', strict_slashes=False)
def catagories_list():
    """ displays a HTML page with a list of states """
    catagories = storage.all(Catagory).values()
    catagories = sorted(catagories, key=lambda k: k.name)
    return render_template('catagories_list.html', catagories=catagories)


if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000)
