from flask import Blueprint, render_template
import pyjokes

app_routes = Blueprint('app_routes', __name__)

@app_routes.route('/')
def home():
    joke = pyjokes.get_joke() # Get a random programming joke
    return render_template('index.html', joke=joke)