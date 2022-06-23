import time

from flask import flash, render_template, url_for, request, session
from flask_login import current_user, login_user, logout_user
from werkzeug.urls import url_parse
from werkzeug.utils import redirect

from app import db
from app.auth import bp
from app.auth.forms import RegistrationForm, LoginForm, SMSForm
from app.models import User
from app.sms import send_sms


@bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    if form.validate_on_submit():
        session['username'] = form.username.data
        session['phone_number'] = form.phone_number.data
        session['code'] = send_sms(session['phone_number'])
        flash(f"Your code is {session['code']}")  # TODO don't forget to disable
        return redirect(url_for('auth.sms'))
    return render_template('auth/register.html', title='Registration page', form=form)


@bp.route('/sms', methods=['GET', 'POST'])
def sms():
    sms_form = SMSForm()
    user = User(username=session['username'], phone_number=session['phone_number'])
    user.set_password(session['phone_number'])
    if request.method == 'POST':
        if request.form['sms'] == 'Register' and sms_form.validate():
            data = sms_form.code_input.data
            db.session.add(user)
            if session['code'] == data:
                db.session.commit()
                login_user(user)
                flash(f'Congratulations, {user.username} you are now a registered user!')
                time.sleep(1)
                return redirect(url_for('main.index'))
            flash('Invalid code. Please try again')
            return render_template('sms.html', sms_form=sms_form)
        elif request.form['sms'] == 'Send SMS':  # TODO change SMS timer value and enable service
            session['code'] = send_sms(session['phone_number'])
            flash(f"Your code is {session['code']}")  # TODO don't forget to disable
            return render_template('sms.html', sms_form=sms_form)
    return render_template('sms.html', sms_form=sms_form)


@bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.phone_number.data):
            flash('Invalid username or phone number')
            return redirect(url_for('auth.login'))
        login_user(user)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('main.index')
        return redirect(next_page)
    return render_template('auth/login.html', title='Sign In', form=form)


@bp.route('/logout')
def logout():
    logout_user()
    session.pop('username', None)
    return redirect(url_for('main.index'))
