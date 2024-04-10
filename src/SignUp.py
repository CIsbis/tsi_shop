import csv
# from src.CustomerLoad import CustomerLoad

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

# Example usage:
sign_up_instance = SignUp("customer.csv")
sign_up_instance.sign_up()
