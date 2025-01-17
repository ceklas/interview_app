import os
import psycopg2
from django.conf import settings

def execute_sql_query(file_path):
    try:
        # Veritabanı bağlantısını kurma
        conn = psycopg2.connect(settings.DATABASE_URL)
        cursor = conn.cursor()

        # SQL dosyasını okuma
        with open(file_path, 'r') as file:
            sql_query = file.read()

        # SQL sorgusunu çalıştırma
        cursor.execute(sql_query)
        conn.commit()  # Değişiklikleri kaydet

        print("SQL sorgusu başarıyla çalıştırıldı.")
    except Exception as e:
        print(f"Bir hata oluştu: {e}")
    finally:
        # Bağlantı ve cursor kapama
        if cursor:
            cursor.close()
        if conn:
            conn.close()