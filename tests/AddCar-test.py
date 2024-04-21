# This class has a single static method cars_add_test(), which writes predefined car 
# details to a CSV file. It uses hard-coded values for make, model, colour, etc., instead of user input.
# The test has stubbing properties as it provides predefined variables 

import csv

make = "Vauxhall"
model = "Corsa"
colour = "Black"
year = "2016"
mileage = "47500"
gearbox = "Manual"
engine_size = "1364"
fuel_type = "petrol"
price = "4495"

class AddCarTest:
    def cars_add_test():
        print("Enter car details")
        with open("test_cars.csv", 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([make, model, colour, year, mileage, gearbox, engine_size, fuel_type, price])

        print("Car added successfully!")

AddCarTest.cars_add_test()