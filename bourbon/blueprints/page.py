"""
page.py

This module holds a blueprint for page-related actions, as well as any database
models.
"""
from flask import Blueprint, render_template
from bourbon import db
from bourbon.blueprints.user import User


# Database models.
class Page(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(256))
    alias = db.Column(db.String(256), unique=True)
    author = db.Column(db.Integer, db.ForeignKey("user.id"))
    revisions = db.relationship("Revision", backref="person", lazy="dynamic")

    def __init__(self, title=None, author=None):
        self.title = title
        self.author = author

        alias = title.replace(" ", "_").replace("'", "")
        self.alias = alias


    def __repr__(self):
        return "<Page \"{0}\">".format(self.title)
    

class Revision(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    page = db.Column(db.Integer, db.ForeignKey("page.id"))
    timestamp = db.Column(db.DateTime(timezone=True))
    author = db.Column(db.Integer, db.ForeignKey("user.id"))

    def __init__(self, page=None, changed_by=None):
        self.page = page
        self.changed_by = changed_by


    def __repr__(self):
        return "<Revision page={0},{1}>".format(self.page, self.changed_by)


# The blueprint definition.
page = Blueprint('page', __name__)


@page.route("/")
def all_pages():
    return render_template("all-pages.html")


@page.route("/<page_id_or_alias>")
def view(page_id):
    return "look at a page"


@page.route("/<page_id_or_alias>/edit")
def edit(page_id):
    return "edit a page"
