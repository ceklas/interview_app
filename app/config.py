#config.py: Uygulama yapılandırmalarını (API anahtarları, veritabanı bağlantısı gibi) içerir.
import os

class Config:
    # Gizli anahtar (Flask güvenliği için gerekli)
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'mysecretkey'  # Çevre değişkeni yoksa varsayılan bir değer kullanılır

    # Veritabanı bağlantı ayarları (SQLite kullanıyoruz)
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///site.db'  # SQLite örneği
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # SQLAlchemy'nin veritabanı değişikliklerini izlememesini sağlarız

    # Diğer isteğe bağlı ayarlar
    # Örneğin, dosya yükleme limiti, e-posta ayarları vb. ekleyebilirsiniz.