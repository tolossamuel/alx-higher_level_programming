#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
num2 = str(number)
num2= int(num2[-1])
if num2 > 5:
    print(f"Last digit of {number:d} is {num2:d} is greater than 5")
elif num2 == 0:
    print(f"Last digit of {number:d} is {num2:d} is 0")
else:
    print(f"Last digit of {number:d} is {num2:d} is less than 6 and not 0")
