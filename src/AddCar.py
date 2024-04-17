import csv



class AddCar:
    def __init__(self, csv_file):
        self.csv_file = csv_file

    def cars_add(self):
        print("Enter car details")
        make = input("Make: ")
        model = input("Model: ")
        colour = input("Colour: ")
        year = input("Year: ")
        mileage = input("Mileage: ")
        gearbox = input("Manual or Automatic: ")
        engine_size = input("Engine size: ")
        fuel_type = input("Fuel type: ")
        price = input("Price: ")

        with open(self.csv_file, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([make, model, colour, year, mileage, gearbox, engine_size, fuel_type, price])

        print("Car added successfully!")

