# Function
from random import random

your_number = input("enter a special number : ")

def calculateRandom(input):
    random_number = random()
    return random_number*float(input)

calculated_number=calculateRandom(your_number)
print(calculated_number)
