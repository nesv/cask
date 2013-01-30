"""
Bourbon is a Flask-powered content management system.
"""
from blueprints.page import page
from flask import Flask
import os
import sys


app = Flask(__name__.split(".")[0])
app.register_blueprint(page)


try:
    from flask.ext.sqlalchemy import SQLAlchemy
except ImportError:
    print "You need to install the Flask-SQLAlchemy extension."
    sys.exit(os.EX_SOFTWARE)

db = SQLAlchemy(app)

@app.route("/")
def home():
    """The index page for Bourbon."""
    return "Grab your flask of bourbon, and have at it!"



