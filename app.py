from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
import requests
import os

app = Flask(__name__)

# Get key
app.config['SECRET_KEY'] = os.environ['EYEBLEACH_SECRET_KEY']

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
@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
