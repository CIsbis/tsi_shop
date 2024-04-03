from ReadCSVFile import ReadCSVFile


class SearchCar:
    def __init__(self, csv_file):
        self.csv_file = csv_file
        self.file_data = ReadCSVFile().get_file_data(self.csv_file)

    def search_car(self):
        make = input("Enter make: ")
        model = input("Enter model: ")
        if make in self.file_data[0] and model in self.file_data[1]:
            print("Car found")
        else:
            print("Car not found")