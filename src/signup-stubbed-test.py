import unittest
from unittest.mock import patch
from SignUp import SignUp
from SignUpStubConfig import StubConfig

class TestSignUp(unittest.TestCase):
    def test_sign_up_with_stubbed_data(self):
        # Stubbed data
        stubbed_data = StubConfig().get_configuration()
        

        # Initialize SignUp instance with stubbed data
        signup = SignUp(csv_file='test.csv')
        signup.email_address = stubbed_data["email_address"]
        signup.first_name = stubbed_data["first_name"]
        signup.last_name = stubbed_data["last_name"]
        signup.password = stubbed_data["password"]

        # Call write to file with stubbed data
        signup.writeToFile( signup.email_address, signup.first_name, signup.last_name, signup.password)

        # Read the test CSV file and verify its content
        with open('test.csv', 'r') as file:
            data_from_file = file.readlines()

        expected_line = ','.join(stubbed_data.values()) + '\n' 
        self.assertIn(expected_line, data_from_file, "Data was not written correctly to the CSV file")

if __name__ == '__main__':
    unittest.main()
