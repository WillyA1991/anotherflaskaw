""" Controller file for Simple Pages HTML pages """
from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

simple_pages = Blueprint('simple_page', __name__,
                        template_folder='templates',static_folder='static')


@simple_pages.route('/', defaults={'page': 'index'})
@simple_pages.route('/<page>')
def show(page):
    """function for properly swapping pages in Simple Pages"""
    # pylint: disable=consider-using-f-string
    try:
        return render_template('%s.html' % page)
    except TemplateNotFound:
        return abort(404)
