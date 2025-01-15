from app import db, create_app
from app.models import *  
from sqlalchemy import inspect


app = create_app()

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Tabloları oluşturuyoruz
        print("Veritabanındaki tablolar:")
        tables = inspect(db.engine).get_table_names()  # Tabloları alıyoruz
        print(tables)  # Tabloları listele

    app.run(debug=True)
    
