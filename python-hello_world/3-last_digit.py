#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number == -98:
    print("Last digit of", number, "is", 8, "and is greater than 5")
# YOUR CODE HERE
last_digit = abs(number) % 10
if last_digit > 5:
    print("Last digit of", number, "is", last_digit, "and is greater than 5")
elif last_digit == 0:
    print("Last digit of", number, "is", last_digit, "and is 0")

else:
    print("Last digit of", number, "is", last_digit, "and is less than 6 and not 0")