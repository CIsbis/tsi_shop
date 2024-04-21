import csv
from AddCar import AddCar

filter_position = ["make","model","colour","year","mileage","gearbox","enginesize","fueltype","price"]
filters = {
    "make":"2",
    "model":"3",
    "colour":"4",
    "year":"5",
    "mileage": "6",
    "gearbox":"7",
    "enginesize": "8",
    "fueltype" : "9",
    "price": "10"
    }

def search_again(car_array, filter):
    answer = input("Search again?\n1. Add another filter\n2. New search\n3. Exit\n")
    if answer == "1":
        for element in filter_position:
            if element == filter.strip().lower():
                del filters[element]
        for key, value in filters.items():
            print(f"{value}. Refine by {key}")
        new_search_int = input("Select an option to refine your search: ")

        if new_search_int in filters.values():
            search_by = [key for key, val in filters.items() if val == new_search_int][0]  # Retrieve the key corresponding to the value
            # Now you can use search_by as the selected filter
            search_input = input(f"Search by {search_by}: ")
            position = filter_position.index(search_by.lower())
            refined_search_results = []
            for car in car_array:
                if car[position].lower() == search_input.lower():
                    refined_search_results.append(car)
            # Display the refined search results
            if refined_search_results:
                print("Cars matching the refined search:")
                for car in refined_search_results:
                    print(car)
                menu()
        else:
            print("Invalid filter option.")
    elif answer == "2":
        search_cars()
    elif answer == "3":
        print("Goodbye")
        exit()


def search_car_logic(filter):    
    with open('src/cars.csv', 'r') as file:
        reader = csv.reader(file)
        found_cars = []

        if filter == "1":
            next(reader)  # Skip the header row
            for row in reader:
                found_cars.append(row)
            print("Here is all cars for sale:")
            for car in found_cars:
                print(car)
            menu()
        else:
            filter_value = next((key for key, value in filters.items() if value == filter), None)
            if filter_value:
                position = filter_position.index(filter_value.lower().strip())
                print(f"Searching by {filter_value}...\n")
                user_search = input(f"Please specify the {filter_value} you wish to search for: ")
                for row in reader:
                    if row:
                        if user_search and row[position].strip().lower() == user_search.strip().lower():
                            found_cars.append(row)
                print("Here is all cars for sale:")
                for car in found_cars:
                    print(car)
                search_again(found_cars,filter_value)
            else:
                print("Please select a valid filter option\n")

def search_cars():
    print("Search for cars\n1. Display all cars\n2. Display by make\n3. Display by model\n4. Display by colour\n5. Display by year\n6. Display by mileage\n7. Display by gearbox\n8. Display by engine size\n9. Display by fuel type\n10. Display by price\n11. Exit")
    option = input("Select an option: ")
    if option == "1":
        print("Displaying all cars...\n")
        search_car_logic(option)
    elif option == "2":
        search_car_logic(option)
    elif option == "3":
        search_car_logic(option)
    elif option == "4":
        search_car_logic(option)
    elif option == "5":
        search_car_logic(option)
    elif option == "6":
        search_car_logic(option)
    elif option == "7":
        search_car_logic(option)
    elif option == "8":
        search_car_logic(option)
    elif option == "9":
        search_car_logic(option)
    elif option == "10":
        search_car_logic(option)
    elif option == "11":
        print("Goodbye")
        exit()
    else:
        print("Please select a valid option\n")
        search_cars()

def menu():
    print("1. Reset and search again\n2. Sell a car\n3. Exit")
    choice = input("Please select: ")
    if choice == "1":
        search_cars()
    elif choice == "2":
        AddCar("cars.csv").cars_add()
    elif choice == "3":
        print("Goodbye")
        exit()

    

    