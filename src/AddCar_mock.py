import unittest
from unittest.mock import patch
from io import StringIO
from AddCar import AddCar  # Replace 'your_module' with the actual module containing AddCar class

class TestAddCar(unittest.TestCase):
    @patch('builtins.input', side_effect=['Toyota', 'Corolla', 'Red', '2020', '5000', 'Automatic', '2.0', 'Petrol', '20000'])
    @patch('csv.writer')
    def test_cars_add(self, mock_csv_writer, mock_input):
        # Initialize AddCar instance
        add_car_instance = AddCar("test_cars.csv")

        # Call cars_add method
        add_car_instance.cars_add()

        # Check that csv.writer was called with the correct arguments
        expected_row = ['Toyota', 'Corolla', 'Red', '2020', '5000', 'Automatic', '2.0', 'Petrol', '20000']
        mock_csv_writer_instance = mock_csv_writer.return_value
        mock_csv_writer_instance.writerow.assert_called_once_with(expected_row)

if __name__ == "__main__":
    unittest.main()
