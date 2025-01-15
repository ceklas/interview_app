from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config,TestingConfig
import os
from dotenv import load_dotenv
from app.models import *

# Veritabanı için SQLAlchemy örneği
#db = SQLAlchemy()

# Çevresel değişkenleri yüklemek için load_dotenv
load_dotenv()  # .env dosyasını yükler

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)  # Config veya özel config sınıfı kullanılır
    print("Veritabanı bağlantı URL'si:", app.config['SQLALCHEMY_DATABASE_URI'])
    db.init_app(app)

    return app

def create_app_with_config(config_class):
     app = Flask(__name__)
     app.config.from_object(config_class)  # config_class ile konfigürasyonu yükle
     db.init_app(app)  # db bağlantısını initialize et

     return app