import logging
import os
from logging.handlers import RotatingFileHandler, SMTPHandler

from flask import render_template

import config
from app import app, db, paranoid, bot


@paranoid.on_invalid_session
def invalid_session():
    return render_template('login.html'), 401


@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    bot.send_message('326063522', 'Check your e-mail')
    return render_template('500.html'), 500


if not app.debug:
    auth = (config.Config.MAIL_USERNAME, config.Config.MAIL_PASSWORD)
    mail_handler = SMTPHandler(
        mailhost=(config.Config.MAIL_SERVER, config.Config.MAIL_PORT),
        fromaddr=config.Config.MAIL_USERNAME,
        toaddrs=config.Config.ADMINS, subject='Customer service Failure',
        credentials=auth, secure=())
    mail_handler.setLevel(logging.ERROR)
    app.logger.addHandler(mail_handler)
    if not os.path.exists('logs'):
        os.mkdir('logs')
    file_handler = RotatingFileHandler('logs/customer_service.log', maxBytes=10240,
                                       backupCount=10)
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.setLevel(logging.INFO)
    app.logger.info('All good')
