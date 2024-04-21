import unittest

class TestCustomer():
    def test_customer_methods(self):
        # Hardcoded values for testing
        first_name = 'Shannon'
        last_name = 'McGurk'
        email = '2038722m@student.gla.ac.uk'
        password = 'password123'

        # Create a TestCustomer instance with hardcoded values
        test_customer = TestCustomer([first_name, last_name, email, password])
        print(test_customer.self(first_name))
        
        # Test the methods
        print(self.assertEqual(test_customer.get_first_name(), first_name))
        self.assertEqual(test_customer.get_last_name(), last_name)
        self.assertEqual(test_customer.get_name(), first_name + " " + last_name)
        self.assertEqual(test_customer.get_email(), email)
        self.assertTrue(test_customer.compare_password(password))
        

if __name__ == '__main__':
    unittest.main()

    
