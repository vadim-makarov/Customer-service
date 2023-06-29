"""Contains an error handler methods"""

from flask import render_template

from app import db, paranoid
from app.errors import bp


@paranoid.on_invalid_session
def invalid_session():
    """Returns a template if 401 error occurs"""
    return render_template('login.html'), 401


@bp.app_errorhandler(404)
def not_found_error(error):
    """Returns a template if 404 error occurs"""
    return render_template('errors/404.html'), 404


@bp.app_errorhandler(500)
def internal_error(error):
    """Restores a DB session and returns a template if 500 error occurs"""
    db.session.rollback()
    bot.send_message('326063522', 'Check your e-mail')
    return render_template('errors/500.html'), 500
