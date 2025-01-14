from app import db
from app.models import Customer
from app import create_app  # Burada create_app fonksiyonunu import ediyoruz
import unittest

class TestDatabase(unittest.TestCase):
    
    def setUp(self):
        # Her testten önce geçici bir veritabanı oluşturur.
        self.app = create_app()  # create_app fonksiyonunu kullanıyoruz
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # Geçici bir veritabanı !!! 
        self.client = self.app.test_client()
        with self.app.app_context():
            db.create_all()  # Tabloları oluştur

    def tearDown(self):
        # Test sonrası veritabanını temizler.
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_add_customer(self):
        # Veritabanına yeni müşteri eklemeyi test et
        with self.app.app_context():
            # Yeni müşteri ekleyelim
            new_customer = Customer(cust_name="Ibrahim Berat Koca", cust_email="ibk@example.com", cust_cont_no=5552223344, cust_addr="Kayseri", cust_type="Retail")
            db.session.add(new_customer)
            db.session.commit()

            # Müşteriyi sorgulayalım
            customer = Customer.query.filter_by(cust_name="Ibrahim Berat Koca").first()
            self.assertIsNotNone(customer)
            self.assertEqual(customer.cust_email, "ibk@example.com")

if __name__ == '__main__':
    unittest.main()