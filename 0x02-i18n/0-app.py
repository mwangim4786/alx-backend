#!/usr/bin/python3
"""Script that starts a Flask web application
"""
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/", methods=['GET'])
def index():
    """Returns string Hello world when route is queried
    """
    return render_template("0-index.html")

if __name__ == "__main__":
    app.run(debug=True)
