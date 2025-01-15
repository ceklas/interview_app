import unittest
from datetime import date
from app.models import *
from app import create_app_with_config, db
from config import TestingConfig  

class TestDatabase(unittest.TestCase):

    def setUp(self):
        # Test için özel bir yapılandırma ile uygulama başlatılır
        self.app = create_app_with_config(TestingConfig)
        self.client = self.app.test_client()
        with self.app.app_context():
            db.create_all()  # Tabloları oluştur

    def tearDown(self):
        # Test sonrası veritabanını temizler
        with self.app.app_context():
            db.session.remove()  # Veritabanı bağlantısını kes
            db.drop_all()  # Tabloları sil

    def test_add_customer(self):
        with self.app.app_context():
            new_customer = Customer(
                cust_name="Ibrahim Berat Koca", 
                cust_email="ibk@example.com", 
                cust_cont_no=5552223344, 
                cust_addr="Kayseri", 
                cust_type="Retail"
            )
            db.session.add(new_customer)
            db.session.commit()

            # Müşteri sorgulama
            customer = Customer.query.filter_by(cust_name="Ibrahim Berat Koca").first()
            self.assertIsNotNone(customer)
            self.assertEqual(customer.cust_email, "ibk@example.com")

    def test_add_employee_details(self):
        with self.app.app_context():
            new_employee = EmployeeDetails(
                emp_name="John Doe", 
                emp_designation="Manager", 
                emp_addr="Istanbul", 
                emp_branch="Branch A", 
                emp_cont_no=5551234567
            )
            db.session.add(new_employee)
            db.session.commit()

            employee = EmployeeDetails.query.filter_by(emp_name="John Doe").first()
            self.assertIsNotNone(employee)
            self.assertEqual(employee.emp_designation, "Manager")

    def test_add_membership(self):
        with self.app.app_context():
            new_membership = Membership(start_date=date(2025, 1, 1), end_date=date(2025, 12, 31))  # datetime.date
            db.session.add(new_membership)
            db.session.commit()

            membership = Membership.query.first()
            self.assertIsNotNone(membership)
            self.assertEqual(membership.start_date, date(2025, 1, 1))  # datetime.date

    def test_add_payment_details(self):
        with self.app.app_context():
            new_payment = PaymentDetails(
                payment_id="PAY12345", 
                shipment_client_c_id=1, 
                shipment_sh_id=1, 
                amount=1000, 
                payment_status="Paid", 
                payment_mode="Card Payment", 
                payment_date=date(2025, 1, 15)  # datetime.date
            )
            db.session.add(new_payment)
            db.session.commit()

            payment = PaymentDetails.query.filter_by(payment_id="PAY12345").first()
            self.assertIsNotNone(payment)
            self.assertEqual(payment.amount, 1000)

    def test_add_shipment_details(self):
        with self.app.app_context():
            new_shipment = ShipmentDetails(
                customer_cust_id=1, 
                sd_content="Electronics", 
                sd_domain="Domestic", 
                sd_type="Express", 
                sd_weight="2kg", 
                sd_charges=150, 
                sd_addr="Istanbul", 
                ds_addr="Kayseri"
            )
            db.session.add(new_shipment)
            db.session.commit()

            shipment = ShipmentDetails.query.filter_by(sd_content="Electronics").first()
            self.assertIsNotNone(shipment)
            self.assertEqual(shipment.sd_charges, 150)

    def test_add_status(self):
        with self.app.app_context():
            new_status = Status(
                current_st="Shipped", 
                sent_date=date(2025, 1, 10),  # datetime.date
                delivery_date=date(2025, 1, 15)  # datetime.date
            )
            db.session.add(new_status)
            db.session.commit()

            status = Status.query.first()
            self.assertIsNotNone(status)
            self.assertEqual(status.current_st, "Shipped")

    def test_add_employee_manages_shipment(self):
        with self.app.app_context():
            new_employee_manages_shipment = EmployeeManagesShipment(
                employee_e_id=1, 
                shipment_sh_id=1, 
                status_sh_id=1
            )
            db.session.add(new_employee_manages_shipment)
            db.session.commit()

            employee_shipment = EmployeeManagesShipment.query.first()
            self.assertIsNotNone(employee_shipment)

if __name__ == '__main__':
    unittest.main()