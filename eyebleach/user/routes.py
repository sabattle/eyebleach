from flask import render_template, url_for, flash, redirect, Blueprint
from eyebleach.user.forms import RegistrationForm, LoginForm
from eyebleach.models import User
from eyebleach import bcrypt

user = Blueprint('user', __name__)

# Registration route
@user.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(form.username.data, form.email.data, hashed_password)
        user.register()
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('main.home'))
    return render_template('register.html', form=form)

# Login route
@user.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('login.html', form=form)
