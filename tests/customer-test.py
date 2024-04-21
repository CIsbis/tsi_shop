# Stub test for Customer Class
# 
import unittest
class Customer:

    first_name_position = 1
    last_name_position = 2
    email_position = 0
    password_position = 3

    def __init__(self, raw_customer):
        self.first_name = raw_customer[self.first_name_position]
        self.last_name = raw_customer[self.last_name_position]
        self.email = raw_customer[self.email_position]
        self.password = raw_customer[self.password_position]

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def get_name(self):
        return self.first_name + " " + self.last_name

    def get_email(self):
        return self.email

    def compare_password(self, password):
        return password == self.password
    
class CustomerTest(unittest.TestCase):
        # Creating a stub raw customer data
    def setUp(self):
        self.stub_customer_data = ["shannon@gmail.com", "Shannon", "McGurk", "password1"]

    def test_initialization(self):
        customer = Customer(self.stub_customer_data)
        self.assertEqual(customer.get_email(), "shannon@gmail.com")
        self.assertEqual(customer.get_first_name(), "Shannon")
        self.assertEqual(customer.get_last_name(), "McGurk")
        self.assertEqual(customer.get_name(), "Shannon McGurk")

    def test_compare_password(self):
        customer = Customer(self.stub_customer_data)
        self.assertTrue(customer.compare_password("password1"))
        self.assertFalse(customer.compare_password("password2"))

if __name__ == "__main__":
    unittest.main()

