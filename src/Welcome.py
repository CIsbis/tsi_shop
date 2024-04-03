from LogIn import LogIn
from ReadCSVFile import ReadCSVFile
from AddCar import AddCar

def Welcome_page():
    print("Welcome to the Car shop")
    print("You can log in or register")
    print("Enter 1 to log in")
    print("Enter 2 to register")
    print("Enter 3 to Search for cars")
    print("Enter 4 to sell a car")
    print("Enter 5 to exit program")
    user_input = input("Enter Number: ")
    return user_input
def user_input(user_input):
    if user_input == "1":
        log_in = LogIn()
        log_in.log_in()
        print("You are logged in")
    elif user_input == "2":
        print("You are registered")
    elif user_input == "3":
        print("Search for cars")
    elif user_input == "4":
        print("Selling a Car")
        add_car = AddCar("cars.csv")
        add_car.cars_add()
    elif user_input == "5":
        print("Goodbye")
    else:
        print("Invalid input")
        user_input(user_input)

Welcome_page(input("Enter Number: "))
