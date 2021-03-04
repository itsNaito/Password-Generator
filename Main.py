#key libraries for the program
import string
import random

#class creates all the random passwords
class passwordManager:
    def __init__(self, text, number, symbol,password):
        self.text = text
        self.number = number
        self.symbol = symbol
        self.password = password
    def textResult(self, length):
        for characters in range(length):
            value = random.randint(0, 51)
            self.password += self.text[value]
        print(self.password)
    def textNumResult(self, length):
        textNum = self.text + self.number
        for characters in range(length):
            value = random.randint(0, 61)
            self.password += textNum[value]
        print(self.password)
    def textNumSymResult(self, length):
        textNumSym = self.text + self.number + self.symbol
        for characters in range(length):
            value = random.randint(0, 93)
            self.password += textNumSym[value]
        print(self.password)

            

#declaration of values in the class
newPassword = passwordManager(string.ascii_uppercase + string.ascii_lowercase, string.digits,  string.punctuation, "")

#start menu
def Main():
    print("1. Create New password")
    print("2. Show Password")
    print("3. quit")
    option = input("Please pick an option ==> ")
    if option == "1":
        generator()
    if option == "2":
        pass
    if option == "3":
        quit()

#gets key parameters for the class to use like the length and what the password will contain
def generator():
    print()
    length = input("How long should the password be ==> ")
    length = int(length)
    print()
    print("1. text")
    print("2. text and numbers")
    print("3. text, numbers, and symbols")
    print()
    container = input("Choose what the password should include ==> ")
    if container == "1":
        newPassword.textResult(length)
    if container == "2":
        newPassword.textNumResult(length)
    if container == "3":
        newPassword.textNumSymResult(length)

Main()