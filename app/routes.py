# -*- coding: utf-8 -*-
import time
from datetime import datetime

from flask import render_template, flash, url_for, request
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse
from werkzeug.utils import redirect

from app import app, db
from app.forms import LoginForm, RegistrationForm, EditProfileForm, Services
from app.models import User, Service


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home page')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    if form.validate_on_submit():
        user = User(username=form.username.data, phone_number=form.phone_number.data)
        user.set_password(form.phone_number.data)
        db.session.add(user)
        db.session.commit()
        login_user(user)
        flash(f'Congratulations, {user.username} you are now a registered user!')
        time.sleep(1)
        return redirect(url_for('index'))
    return render_template('register.html', title='Registration page', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.phone_number.data):
            flash('Invalid username or phone_number')
            return redirect(url_for('login'))
        login_user(user)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/user/<username>', methods=['GET', 'POST'])
@login_required
def user(username):
    form = Services()
    user = User.query.filter_by(username=username).first()
    services = Service.query.filter_by(user_id=user.id)
    if form.validate_on_submit():
        user_choises = ' '.join([form.service1.data, form.service2.data, form.service3.data])
        service_add = Service(service=user_choises, service_time=form.service_time.data, user_id=user.id)
        db.session.add(service_add)
        db.session.commit()
        flash(f'Congratulations, {user.username} you are registered for service at {service_add.service_time}!')
        time.sleep(1)
        return render_template('user.html', user=user, title=username, form=form, services=services)
    return render_template('user.html', user=user, title=username, form=form, services=services)


@app.route('/user/<int:service_id>', methods=['POST'])
@login_required
def delete_service(service_id):
    service_del = Service.query.get_or_404(service_id)
    db.session.delete(service_del)
    db.session.commit()
    flash('Item deleted.')
    return render_template('user.html', user=user)


@app.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.today()
        db.session.commit()


@app.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm(current_user.username, current_user.phone_number)
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.phone_number = form.phone_number.data
        current_user.about_me = form.about_me.data
        db.session.commit()
        flash('Your changes have been saved.')
        time.sleep(1)
        return redirect(url_for('user', username=current_user.username))  # return to user's profile page
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.phone_number.data = current_user.phone_number
        form.about_me.data = current_user.about_me
    return render_template('edit_profile.html', title='Edit Profile',
                           form=form)
