from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app import app
from config import Config

app.config['SECRET_KEY'] = 'I-cant-talk-about-this'

if __name__ == '__main__':
    app.run(debug=True)