# -*- coding: utf-8 -*-
import time
from datetime import datetime

from flask import render_template, flash, url_for
from flask_login import current_user
from werkzeug.utils import redirect

from app import db
from app.main import bp
from app.main.forms import Reviews
from app.models import Review


@bp.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.now().date()
        db.session.commit()


@bp.route('/')
@bp.route('index')
def index():
    return render_template('index.html', title='Home page')


@bp.route('/pricing')
def pricing():
    return render_template('pricing.html', title='Pricing')


@bp.route('/reviews', methods=['GET', 'POST'])
def reviews():
    form = Reviews()
    all_reviews = Review.query.order_by(Review.review_date.desc()).all()
    if form.validate_on_submit():
        review = Review(author=current_user, text=form.text.data, rating=form.rating.data)
        db.session.add(review)
        db.session.commit()
        flash("Thank you for your feedback."
              "We're getting better because of you.")
        time.sleep(0.5)
        return redirect(url_for('main.reviews'))
    return render_template('reviews.html', title='Reviews', form=form, all_reviews=all_reviews)


@bp.route('/features')
def features():
    return render_template('features.html', title='Features')


@bp.route('/modal')
def modal():
    return render_template('modal.html', title='Modal')
