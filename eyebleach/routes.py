from flask import render_template, url_for, flash, redirect
from eyebleach.forms import RegistrationForm, LoginForm
from eyebleach import app
import requests

# Home route
@app.route('/')
@app.route('/home')
def home():
    res = requests.get('https://random.dog/woof.json')
    image_url = res.json()['url']
    return render_template('index.html', image=image_url)

# About route
@app.route('/about')
def about():
    return render_template('about.html', title='About')

# Registration route
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', form=form)

# Login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('login.html', form=form)
