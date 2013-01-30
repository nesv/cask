"""
page.py

This module holds a blueprint for page-related actions.
"""

from flask import Blueprint


page = Blueprint('page', __name__)


@page.route("/pages/<page_id>")
def view(page_id):
    return "look at a page"


@page.route("/pages/<page_id>/edit")
def edit(page_id):
    return "edit a page"
