from flask import render_template

from app import db, paranoid, bot
from app.errors import bp


@paranoid.on_invalid_session
def invalid_session():
    return render_template('login.html'), 401


@bp.app_errorhandler(404)
def not_found_error(error):
    return render_template('errors/404.html'), 404


@bp.app_errorhandler(500)
def internal_error(error):
    db.session.rollback()
    bot.send_message('326063522', 'Check your e-mail')
    return render_template('errors/500.html'), 500


