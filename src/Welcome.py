import csv
from LogIn import LogIn
from AddCar import AddCar

class SignUp:
    def __init__(self, csv_file):
        self.csv_file = csv_file

    def sign_up(self):
        email_address = input("Enter your email address: ")
        first_name = input("Enter your first name: ")
        last_name = input("Enter your last name: ")
        password = input("Enter password: ")

        # Write the email and password to the CSV file
        with open(self.csv_file, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([email_address, first_name, last_name, password])
        print("Signed up successfully!")
        Welcome().get_logged_in_user_input()  # Corrected method invocation
    

class Welcome:
    @staticmethod
    def handle_non_logged_in_user_input(user_input):
        if user_input == "1":
            LogIn().log_in()
            Welcome().get_logged_in_user_input()
        elif user_input == "2":
            SignUp("customer.csv").sign_up()
        elif user_input == "3":
            print("Goodbye")
            exit()
        else:
            print("Invalid input. Please try again.")

    @staticmethod
    def get_user_input_welcome():
        print("Welcome to the Car shop")
        print("Before you start browsing we need you to log in."
            " If you do not have an account, you can register.")
        print("Enter 1 to log in")
        print("Enter 2 to register")
        print("Enter 3 to exit program")
        user_input = input("Enter Number: ")
        Welcome().handle_non_logged_in_user_input(user_input)  # Corrected method invocation

    @staticmethod
    def get_logged_in_user_input():
        #print("You're in! Now you can browse the cars we have on offer or put your cars up for sale.")
        print("Enter 1 to browse our cars")
        print("Enter 2 to put your car up for sale")
        print("Enter 3 to exit program")
        user_input = input("Enter Number: ")
        Welcome().handle_logged_in_user_input(user_input)  # Corrected method invocation

    @staticmethod
    def handle_logged_in_user_input(user_input):
        if user_input == "1":
            print("You can browse our cars")
            from SearchCar import search_cars
            search_cars()
        elif user_input == "2":
            AddCar("cars.csv").cars_add()
        elif user_input == "3":
            print("Goodbye")
            exit()
        else:
            print("Invalid input. Please try again.")
            Welcome().get_logged_in_user_input()  # Corrected method invocation

Welcome().get_user_input_welcome()  # Corrected method invocation
