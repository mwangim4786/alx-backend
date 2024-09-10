from flask import Blueprint, render_template

app_routes = Blueprint("app_routes", __name__, template_folder="templates")

@app_routes.route("/")
def index():
    return render_template("0-index.html")
