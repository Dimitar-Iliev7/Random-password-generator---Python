# ask the user if they want to generate a password or not
# if yes, ask for password length
# generate password
# print password
# if no, exit the program

import string
import random

charecters = list(string.ascii_letters + string.digits + "!@#$%^&*()")

def generate_password():
    password_length = int(input("How long would you like your password to be? "))

    random.shuffle(charecters)

    password = []

    for x in range(password_length):
        password.append(random.choice(charecters))

    random.shuffle(password)

    password = "".join(password)

    print(password)

option = input("Do you want to generate a password? (Yes/No) ")

if option == "Yes":
    generate_password()
elif option == "No":
    print("Program ended")
    quit()
else:
    print("Invalid input, please input Yes or No")
    quit()