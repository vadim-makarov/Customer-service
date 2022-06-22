# -*- coding: utf-8 -*-
import time
from datetime import datetime

from flask import render_template, flash, url_for, request, session
from flask_login import current_user, login_required
from werkzeug.utils import redirect

from app import app, db
from app.forms import EditProfileForm, Services, SMSForm, Reviews
from app.models import User, Service, Review
from app.sms import send_sms, reminder


@app.route('/')
@app.route('/index')
def index():
    if datetime.now().minute == 25:
        reminder()
    return render_template('index.html', title='Home page')


@app.route('/user/<username>', methods=['GET', 'POST'])
@app.route('/user')
@login_required
def user(username):
    if not current_user.is_authenticated:
        return redirect(url_for('register'))
    form = Services()
    user = User.query.filter_by(username=username).first()
    date = datetime.now().date()  # hide old records
    services = Service.query.filter_by(user_id=user.id)
    profile_form = EditProfileForm(current_user.username, current_user.phone_number)
    if profile_form.validate_on_submit():  # edit profile
        session['username'] = profile_form.username.data
        session['phone_number'] = profile_form.phone_number.data
        session['code'] = send_sms(session['phone_number'])
        flash(f"Your code is {session['code']}")
        return redirect(url_for('edit_sms'))
    elif request.method == 'GET':
        profile_form.username.data = current_user.username
        profile_form.phone_number.data = current_user.phone_number
    return render_template('user.html', user=user, title=username, form=form, profile_form=profile_form,
                           services=services, date=date)


@app.route('/edit_sms', methods=['GET', 'POST'])
def edit_sms():
    sms_form = SMSForm()
    current_user.username = session['username']
    current_user.phone_number = session['phone_number']
    current_user.set_password(session['phone_number'])
    if request.method == 'POST':
        if request.form['sms'] == 'Register' and sms_form.validate():
            data = sms_form.code_input.data
            if session['code'] == data:
                db.session.commit()
                flash(f'Values has been changed')
                time.sleep(1)
                return redirect(url_for('user', username=current_user.username))
            flash('Invalid code. Please try again')
            return render_template('sms.html', sms_form=sms_form)
        elif request.form['sms'] == 'Send SMS':  # TODO change SMS timer value and enable service
            session['code'] = send_sms(session['phone_number'])
            flash(f"Your code is {session['code']}")  # don't forget to disable
            return render_template('sms.html', sms_form=sms_form)
    return render_template('sms.html', sms_form=sms_form)


@app.route('/user/add_service', methods=['POST'])
@login_required
def add_service():
    form = Services()
    if form.validate_on_submit():
        service_add = Service(service1=form.service1.data, service2=form.service2.data,
                              service3=form.service3.data,
                              service_date=form.service_date.data,
                              service_time=form.service_time.data, user_id=current_user.id)
        db.session.add(service_add)
        db.session.commit()
        flash(f'Congratulations, {current_user.username} you are registered for service at {service_add.service_time}!')
        time.sleep(1)
        return redirect(url_for('user', username=current_user.username))
    flash('This date or time are already in use. Please choose another date or time.')
    return redirect(url_for('user', username=current_user.username))


@app.route('/edit_service/<int:service_id>', methods=['GET', 'POST'])
@login_required
def edit_service(service_id=None):
    if service_id is not None:
        service = Service.query.filter_by(id=service_id).first()
        form = Services()
        if form.validate_on_submit():
            service.service1 = form.service1.data
            service.service2 = form.service2.data
            service.service3 = form.service3.data
            service.service_date = form.service_date.data
            service.service_time = form.service_time.data
            db.session.commit()
            flash(
                f'Ok, {current_user.username} you have changed your service to on {service.service_date} at {service.service_time}!')
            time.sleep(0.5)
            return redirect(url_for('user', username=current_user.username))
        flash('This date or time are already in use. Please choose another date or time.')
    return redirect(url_for('user', username=current_user.username))


@app.route('/user/<int:service_id>', methods=['POST'])
@login_required
def delete_service(service_id):
    service_del = Service.query.get_or_404(service_id)
    db.session.delete(service_del)
    db.session.commit()
    flash('Item deleted.')
    return redirect(url_for('user', username=current_user.username))


@app.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.now().date()
        db.session.commit()


@app.route('/pricing')
def pricing():
    return render_template('pricing.html', title='Pricing')


@app.route('/reviews', methods=['GET', 'POST'])
def reviews():
    form = Reviews()
    all_reviews = Review.query.order_by(Review.review_date.desc()).all()
    if form.validate_on_submit():
        review = Review(author=current_user.username, text=form.text.data, rating=form.rating.data)
        db.session.add(review)
        db.session.commit()
        flash("Thank you for your feedback."
              "We're getting better because of you.")
        time.sleep(0.5)
        return redirect(url_for('reviews'))
    return render_template('reviews.html', title='Reviews', form=form, all_reviews=all_reviews)


@app.route('/features')
def features():
    return render_template('features.html', title='Features')


@app.route('/modal')
def modal():
    return render_template('modal.html', title='Modal')
