import csv
# from src.CustomerLoad import CustomerLoad

class SignUp:
    email_address = ""
    first_name = ""
    last_name = ""
    password = ""
    csv_file = ""
    
    def __init__(self, csv_file):
        self.csv_file = csv_file

    def sign_up(self):
        self.email_address = input("Enter your email address: ")
        self.first_name = input("Enter your first name: ")
        self.last_name = input("Enter your last name: ")
        self.password = input("Enter password: ")
        self.writeToFile(self.email_address,self.first_name, self.last_name, self.password)

        # Write the email and password to the CSV file
        
    def writeToFile(self, email_address, first_name, last_name, password):
        with open(self.csv_file, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([email_address, first_name, last_name, password])

            return print("Signed up successfully!")

