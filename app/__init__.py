from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from dotenv import load_dotenv
from app.models import *

# Veritabanı için SQLAlchemy örneği
#db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    #load_dotenv()  # .env dosyasını yükler

    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

    db.init_app(app)

    # Basit bir rota ekleyelim
    @app.route('/')
    def home():
        return 'Welcome to the Interview App!'

    return app