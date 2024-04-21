from unittest.mock import patch, MagicMock
import unittest
import csv
from SignUp import SignUp

class TestSignUp(unittest.TestCase):

    @patch('builtins.input', side_effect=["test@mail.com", "John", "Doe", "1234"])
    def test_sign_up(self, mocked_input):
        # Prepare a test CSV file
        test_csv_file = 'test_customer.csv'

        # Initialize SignUp
        sign_up_instance = SignUp(csv_file=test_csv_file)

        # Call the sign_up() method
        sign_up_instance.sign_up()

        # Read the test CSV file and verify its content
        with open(test_csv_file, 'r') as file:
            reader = csv.reader(file)
            rows = list(reader)
            expected_data = ["test@mail.com", "John", "Doe", "1234"]
            self.assertEqual(rows[-1], expected_data, "Data was not written correctly to the CSV file")

if __name__ == '__main__':
    unittest.main()
