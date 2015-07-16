# coding=utf-8

from flask import render_template, current_app, request
from . import main
from ..helpers.search_helpers import get_template_data


@main.app_errorhandler(404)
def page_not_found(e):
    template_data = get_template_data(main, {})
    return render_template("errors/404.html", **template_data), 404


@main.app_errorhandler(500)
def page_not_found(e):
    template_data = get_template_data(main, {})
    return render_template("errors/500.html", **template_data), 500
