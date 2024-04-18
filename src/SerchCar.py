from ReadCSVFile import ReadCSVFile


def search_car_logic(make=None, color=None, model=None, automatic_or_manual=None, electric_or_not=None, mileage=None,
                     year=None):
    found_cars = ReadCSVFile().get_file_data('cars.csv')
    filtered_cars = []

    for row in found_cars:
        if row:
            if make and row[0].strip().lower() == make.strip().lower():
                filtered_cars.append(row)
            elif color and row[2].strip().lower() == color.strip().lower():
                filtered_cars.append(row)
            elif model and row[1].strip().lower() == model.strip().lower():
                filtered_cars.append(row)
            elif automatic_or_manual and row[5].strip().lower() == automatic_or_manual.strip().lower():
                filtered_cars.append(row)
            elif electric_or_not and row[7].strip().lower() == electric_or_not.strip().lower():
                filtered_cars.append(row)
            elif mileage and row[4].strip().lower() == mileage.strip().lower():
                filtered_cars.append(row)
            elif year and row[3].strip().lower() == year.strip().lower():
                filtered_cars.append(row)
    return filtered_cars


def search_cars():
    make = input("Enter the make of the car you want to search for (leave empty to skip): ").strip()
    color = input("Enter the color of the car you want to search for (leave empty to skip): ").strip()
    model = input("Enter the model of the car you want to search for (leave empty to skip): ").strip()
    automatic_or_manual = input("Enter if you want the search to show you automatic or manual cars "
                                "(leave empty to skip): ").strip()
    electric_or_not = input("Enter if you want the search to show you electric, petrol or diesel cars"
                            " (leave empty to skip): ").strip()
    mileage = input("Enter the mileage of the car you want to search for (leave empty to skip): ").strip()
    year = input("Enter the year of the car you want to search for (leave empty to skip): ").strip()

    results = search_car_logic(make, color, model, automatic_or_manual, electric_or_not, mileage, year)

    if results:
        if make:
            print(f"Found {len(results)} cars matching the make '{make}':")
        elif color:
            print(f"Found {len(results)} cars matching the color '{color}':")
        elif model:
            print(f"Found {len(results)} cars matching the model '{model}':")
        elif automatic_or_manual:
            print(f"Found {len(results)} cars matching the automatic or manual '{automatic_or_manual}':")
        elif electric_or_not:
            print(f"Found {len(results)} cars matching the electric or not '{electric_or_not}':")
        elif mileage:
            print(f"Found {len(results)} cars matching the mileage '{mileage}':")
        elif year:
            print(f"Found {len(results)} cars matching the year '{year}':")

        for car in results:
            print(car)
    else:
        print("No cars found.")
