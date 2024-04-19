import unittest
from unittest.mock import patch
from io import StringIO
from SignUp import SignUp

class TestSignUp(unittest.TestCase):
    @patch('builtins.input', side_effect=['test@example.com', 'John', 'Doe', 'password123'])
    @patch('csv.writer')
    def test_sign_up(self, mock_csv_writer, mock_input):

        sign_up_instance = SignUp("customer.csv")


        sign_up_instance.sign_up()

        expected_row = ['test@example.com', 'John', 'Doe', 'password123']
        mock_csv_writer_instance = mock_csv_writer.return_value
        mock_csv_writer_instance.writerow.assert_called_once_with(expected_row)

        self.assertEqual(mock_input.call_count, 4)  # Ensure input is called 4 times
        self.assertEqual(sign_up_instance.sign_up(), "Signed up successfully!")

if __name__ == "__main__":
    unittest.main()


