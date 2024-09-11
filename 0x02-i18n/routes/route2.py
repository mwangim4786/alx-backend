#!/usr/bin/env python3
""" Route task 2 """
from flask import Blueprint, render_template

app_routes = Blueprint('app_routes', __name__, template_folder="templates")


@app_routes.route('/')
def home():
    """ Home page """
    return render_template('2-index.html')
