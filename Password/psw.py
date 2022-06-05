import random

print("Welcome to Spetsam's password generator.")

chars = str(print("Input the characters you would like to be featured in your password.")) #As a string

number = input("How many passwords do you want to generate? ")
number = int(number) #Converting to integer

length = input("What is your password length? Make sure to have a sufficient number based on your previous input. ")
length = int(length)

print("\nYour passwords have been generated: ")

for pwd in range(number):
    passwords = '' #Empty for initialization
    for c in range(length):
        passwords += random.choice(chars) #For chars chosen by user
    print(passwords)