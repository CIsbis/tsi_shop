import csv


class AddCar:
    def __init__(self, csv_file):
        self.csv_file = csv_file

    def cars_add(self):
        print("Enter car details")
        make = input("Make: ")
        model = input("Model: ")
        year = input("Year: ")
        mileage = input("Mileage: ")
        gearbox = input("Manual or Automatic: ")
        price = input("Price: ")


        # Write the email and password to the CSV file
        with open(self.csv_file, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([make, model, year,mileage, gearbox, price])

        print("Signed up successfully!")

# Example usage:
add_car_instance = AddCar("cars.csv")
add_car_instance.cars_add()