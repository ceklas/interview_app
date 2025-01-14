import os

class Config:
    # Secret Key(Flask güvenliği için gerekli)
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'mysecretkey'  # Çevre değişkeni yoksa varsayılan bir değer kullanılır

    # Veritabanı bağlantı ayarları (PostgreSQL kullanıyoruz)
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///site.db'  # .env'den al, yoksa varsayılan SQLite kullan
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # SQLAlchemy'nin veritabanı değişikliklerini izlememesini sağlarız

