"""
Bourbon is a Flask-powered content management system.
"""
from flask import Flask, render_template
import os
import sys
try:
    from flask.ext.sqlalchemy import SQLAlchemy
except ImportError:
    print "You need to install the Flask-SQLAlchemy extension."
    sys.exit(os.EX_SOFTWARE)

app = Flask(__name__.split(".")[0])
db = SQLAlchemy(app)

from blueprints.page import page
app.register_blueprint(page, url_prefix="/pages")

from blueprints.user import user
app.register_blueprint(user)


@app.route("/")
def home():
    """Loads the index page."""
    return render_template("index.html")
