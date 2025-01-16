from django.test import TestCase
from datetime import date
from app.models import *  # Modelleri buraya eklediğinizden emin olun

class TestDatabase(TestCase):

    def test_add_customer(self):
        customer = Customer.objects.create(
            cust_name="Ibrahim Berat Koca", 
            cust_email="ibk@example.com", 
            cust_cont_no=5552223344, 
            cust_addr="Kayseri", 
            cust_type="Retail"
        )
        self.assertEqual(customer.cust_name, "Ibrahim Berat Koca")

    def test_add_shipment(self):
        # İlk önce müşteri oluşturulmalı
        customer = Customer.objects.create(
            cust_name="Ibrahim Berat Koca", 
            cust_email="ibk@example.com", 
            cust_cont_no=5552223344, 
            cust_addr="Kayseri", 
            cust_type="Retail"
        )
        
        shipment = Shipment.objects.create(
            customer=customer,  # Müşteri ile ilişkilendirme
            sd_content="Electronics", 
            sd_domain="Domestic", 
            sd_type="Express", 
            sd_weight="2kg", 
            sd_charges=150, 
            sd_addr="Istanbul", 
            ds_addr="Kayseri"
        )
        self.assertEqual(shipment.sd_content, "Electronics")

    def test_add_payment_details(self):
        # İlk önce müşteri oluşturulmalı
        customer = Customer.objects.create(
            cust_name="Ibrahim Berat Koca", 
            cust_email="ibk@example.com", 
            cust_cont_no=5552223344, 
            cust_addr="Kayseri", 
            cust_type="Retail"
        )
    
        # Gönderi oluşturulmalı
        shipment = Shipment.objects.create(
            customer=customer,  # Müşteri ile ilişkilendirme
            sd_content="Electronics", 
            sd_domain="Domestic", 
            sd_type="Express", 
            sd_weight="2kg", 
            sd_charges=150, 
            sd_addr="Istanbul", 
            ds_addr="Kayseri"
        )
    
        # Ödeme detaylarını oluşturma
        new_payment = PaymentDetails.objects.create(
            payment_id="PAY12345", 
            shipment=shipment,  # Gönderi ile ilişkilendirme
            customer=customer,  # Müşteri ile ilişkilendirme (eğer modelde bir ilişki varsa)
            amount=1000, 
            payment_status="Paid", 
            payment_mode="Card Payment", 
            payment_date=date(2025, 1, 15)
        )
    
        # Testler
        self.assertEqual(new_payment.payment_id, "PAY12345")
        self.assertEqual(new_payment.amount, 1000)
        self.assertEqual(new_payment.payment_status, "Paid")
        self.assertEqual(new_payment.payment_mode, "Card Payment")