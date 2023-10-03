#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
number = str(number)
number = int(number[-1])
if number > 5:
    print(f"{number:d} is greater than 5")
elif number == 0:
    print(f"{number:d} is 0")
else:
    print(f"{number} is less than 6 and not 0")
