import os

class Config:
    # Secret Key (Flask güvenliği için gerekli)
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'mysecretkey'  # Çevre değişkeni yoksa varsayılan bir değer kullanılır

    # Veritabanı bağlantı ayarları (PostgreSQL kullanıyoruz)
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgresql://postgres:798798i.@127.0.0.1:5432/interview_app_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # SQLAlchemy'nin veritabanı değişikliklerini izlememesini sağlarız

    # Test ortamı için özel ayarlar
    TESTING = False
    SQLALCHEMY_DATABASE_URI_TEST = os.environ.get('DATABASE_URL_TEST') or 'sqlite:///:memory:'  # Bellek içi SQLite veritabanı

# Test ortamı için config sınıfı
class TestingConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'  # Test veritabanı
    TESTING = True  # Test modunu aktif yap
    SQLALCHEMY_TRACK_MODIFICATIONS = False