from flask import render_template, Blueprint
import requests

main = Blueprint('main', __name__)

# Home route
@main.route('/')
@main.route('/home')
def home():
    res = requests.get('https://random.dog/woof.json')
    image_url = res.json()['url']
    return render_template('index.html', image=image_url)

# About route
@main.route('/about')
def about():
    return render_template('about.html', title='About')
