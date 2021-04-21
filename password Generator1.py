"""
coded by awetz
my first script ^_^

"""

import random
import string
import os

password = []
letters = string.ascii_letters
numbers = string.digits
symbols = string.punctuation

try:
    input_letters = int(input("How many letters you want ?: "))
except:
    print ("Please enter number!")
    exit()

try:
    input_numbers = int(input("How many numbers you want ?: "))
except:
    print ("Please enter number!")
    exit()

try:
    input_symbol = int(input("How many symbols you want ?: "))
except:
    print ("Please enter number!")
    exit()

for z in range(input_letters):
    n = random.choice(letters)
    password.append(n)

for x in range(input_numbers):
    n = random.choice(numbers)
    password.append(n)

for c in range(input_symbol):
    n = random.choice(symbols)
    password.append(n)

password = "".join(password)

if system() == "Windows":
    os.system("cls")
elif system() == "Linux":
    os.system("clear")
else:
    print("Please use windows/linux")

print("Done !")
print("Your password is ---> ",password," <---")
