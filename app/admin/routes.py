"""Contains admin page routes"""

from flask import url_for
from flask_login import login_required, current_user
from werkzeug.utils import redirect

from app import db
from app.admin import bp
from app.admin.models import CustomerServiceView
from app.models import User


@bp.route('/')
@bp.route('index')
@login_required
def admin():
    """returns an admin page template"""
    if current_user.is_authenticated:
        if current_user.username == 'VadimM':
            return CustomerServiceView(User, db.session).render('index.html')
        return redirect(url_for('main.index'))
    return redirect(url_for('auth.login'))
