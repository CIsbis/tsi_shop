import csv


def search_car_logic(make=None, color=None):
    with open('cars.csv', 'r') as file:
        reader = csv.reader(file)
        found_cars = []
        for row in reader:
            if row:
                if make and row[0].strip().lower() == make.strip().lower():
                    found_cars.append(row)
                elif color and row[2].strip().lower() == color.strip().lower():
                    found_cars.append(row)
        return found_cars


def search_cars():
    make = input("Enter the make of the car you want to search for (leave empty to skip): ").strip()
    color = input("Enter the color of the car you want to search for (leave empty to skip): ").strip()

    results = search_car_logic(make, color)
    if results:
        if make:
            print(f"Found {len(results)} cars matching the make '{make}':")
        if color:
            print(f"Found {len(results)} cars matching the color '{color}':")
        for car in results:
            print(car)
    else:
        print("No cars found.")

