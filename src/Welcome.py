from LogIn import LogIn
from AddCar import AddCar
from SignUp import SignUp


def get_user_input_welcome():
    print("Welcome to the Car shop")
    print("Before you start browsing we need you to log in."
          " If you do not have an account, you can register.")
    print("Enter 1 to log in")
    print("Enter 2 to register")
    print("Enter 3 to exit program")
    user_input = input("Enter Number: ")
    return user_input


def handle_non_logged_in_user_input():
    user_input = get_user_input_welcome()
    while user_input not in ["1", "2", "3"]:
        if user_input == "1":
            LogIn().log_in()
            print("You are logged in!")

        elif user_input == "2":
            SignUp().sign_up()
            print("You have been registered successfully!")
        elif user_input == "3":
            print("Goodbye")
            exit()
        else:
            print("Invalid input. Please try again.")
            user_input = get_user_input_welcome()


def get_logged_in_user_input():
    print("Your in! Now you can browse the cars we have on offer or put your cars up for sale.")
    print("Enter 1 to browse our cars")
    print("Enter 2 to put your car up for sale")
    print("Enter 3 to exit program")
    user_input = input("Enter Number: ")
    return user_input


def handle_logged_in_user_input():
    user_input = get_logged_in_user_input()
    while user_input not in ["1", "2", "3"]:
        if user_input == "1":
            print("You can browse our cars")
        elif user_input == "2":
            AddCar().cars_add()
        elif user_input == "3":
            print("Goodbye")
            exit()
        else:
            print("Invalid input. Please try again.")
            user_input = get_logged_in_user_input()



