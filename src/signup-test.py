from unittest import TestCase
import SignUpStubConfig
import SignUp
import ReadCSVFile



def TestSignUp(self):
    stub = SignUpStubConfig()
    stubbedData = stub.get_configuration(stub)
    
    signup = SignUp()
    signup.email_address = stubbedData.email_address
    signup.first_name = stubbedData.first_name
    signup.last_name = stubbedData.last_name
    signup.password = stubbedData.password
    
    signup.writeToFile(signup.email_address, signup.first_name, signup.last_name, signup.password)
    # to do read back file to verify correct sign up
    
    reader = ReadCSVFile()
    dataFromFile = reader.get_file_data(reader, "customer.csv")
    
    self.assertEqual(stubbedData, dataFromFile,"not eqaul")
    
    
    
    
    