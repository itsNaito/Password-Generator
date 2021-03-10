#key libraries for the program
import string
import random
import os.path
from os import path
from cryptography.fernet import Fernet

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
        confirm()

    def textNumResult(self, length):
        textNum = self.text + self.number
        for characters in range(length):
            value = random.randint(0, 61)
            self.password += textNum[value]
        print(self.password)
        confirm()
        
    def textNumSymResult(self, length):
        textNumSym = self.text + self.number + self.symbol
        for characters in range(length):
            value = random.randint(0, 93)
            self.password += textNumSym[value]
        print(self.password)
        confirm()
#class that creates files that hold the password
class files(passwordManager):
    def __init__(self, title,passwordManager):
        self.title = title
        self.password = passwordManager.password
    
    def newFile(self):
        f = open(self.title, 'w+')
        f.write(self.password)
        f.close()
        print("password saved")

#used to handle on the encryption and decryption
class crypting():
    def __init__(self,files,passwordManager):
        self.title = files.title
        self.password = passwordManager.password
        pass

    def openKey(self):
        spawn = path.exists("secret.key")
        if spawn == False:
            key = Fernet.generate_key()
            f = open("secret.key","wb")
            f.write(key)
            f.close()
            crypting.encrypting(self)
    
    def encrypting(self):
        f = open("secret.key","rb")
        key = f.read()
        f.close()
        ##
        currentPassword = self.password.encode()
        f = Fernet(key)
        encryptPassword = f.encrypt(currentPassword)
        print(encryptPassword)



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
    print("4. quit")
    print()
    container = input("Choose what the password should include ==> ")
    if container == "1":
        newPassword.textResult(length)
    if container == "2":
        newPassword.textNumResult(length)
    if container == "3":
        newPassword.textNumSymResult(length)
    if container == "4":
        quit()
#checks with the user before pushing password into file and gives the file a name 
def confirm():
    approval = input("Are u happy with this password ==> ")
    if approval == 'y' or 'yes':
        createTitle = input("What is the use for this password ==> ")
        createTitle += ".txt"
        createFile = files(createTitle, newPassword)
        newCryption = crypting(createFile, newPassword) 
        newCryption.openKey()
    elif approval == 'n' or 'no':
        pass


Main()