from flask import Flask, Blueprint, render_template, g, flash
from flask import jsonify, redirect, request, url_for

# Load our BluePrints
from jumper.blueprints import blueprint_api

# Create our Flask object and register the blueprints on it
app = Flask(__name__)
app.register_blueprint(blueprint_api)

# Load our views which
from jumper.views import IndexForm

# @app.context_processor
# def inject_test_cities_template():
#     return dict(test_cities=cities)


@app.route("/", methods=["GET", "POST"])
def index():

    form = IndexForm(request.form)

    if request.method == "POST" and form.validate():
        flash("Click the buttons!")

    return render_template("index.html", form=form)