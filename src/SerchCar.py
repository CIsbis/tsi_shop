from ReadCSVFile import ReadCSVFile


def search_car_logic(filters):
    found_cars = ReadCSVFile().get_file_data('cars.csv')
    filtered_cars = []

    for row in found_cars:
        if row:
            if any(filter_func(row) for filter_func in filters):
                filtered_cars.append(row)
    return filtered_cars


def make_filter_functions(filters):
    filter_functions = []
    for filter_name, filter_value in filters:
        if filter_name == 'make':
            filter_functions.append(lambda row: row[0].strip().lower() == filter_value.strip().lower())
        elif filter_name == 'color':
            filter_functions.append(lambda row: row[2].strip().lower() == filter_value.strip().lower())
        elif filter_name == 'model':
            filter_functions.append(lambda row: row[1].strip().lower() == filter_value.strip().lower())
        elif filter_name == 'automatic_or_manual':
            filter_functions.append(lambda row: row[5].strip().lower() == filter_value.strip().lower())
        elif filter_name == 'electric_or_not':
            filter_functions.append(lambda row: row[7].strip().lower() == filter_value.strip().lower())
        elif filter_name == 'mileage':
            filter_functions.append(lambda row: row[4].strip().lower() == filter_value.strip().lower())
        elif filter_name == 'year':
            filter_functions.append(lambda row: row[3].strip().lower() == filter_value.strip().lower())
    return filter_functions


def search_cars():
    filters = []
    filters.append(('make', input("Enter the make of the car you want to search for (leave empty to skip): ").strip()))
    filters.append(('color', input("Enter the color of the car you want to search for (leave empty to skip): ").strip()))
    filters.append(('model', input("Enter the model of the car you want to search for (leave empty to skip): ").strip()))
    filters.append(('automatic_or_manual', input("Enter if you want the search to show you automatic or manual cars "
                                                 "(leave empty to skip): ").strip()))
    filters.append(('electric_or_not', input("Enter if you want the search to show you electric, petrol or diesel cars"
                                             " (leave empty to skip): ").strip()))
    filters.append(('mileage', input("Enter the mileage of the car you want to search for (leave empty to skip): ").strip()))
    filters.append(('year', input("Enter the year of the car you want to search for (leave empty to skip): ").strip()))

    filters = [(name, value) for name, value in filters if value]

    if not filters:
        print("No filters provided.")
        return

    filter_functions = make_filter_functions(filters)

    results = search_car_logic(filter_functions)

    if results:
        print(f"Found {len(results)} cars matching the filters:")
        for car in results:
            print(car)
    else:
        print("No cars found.")
