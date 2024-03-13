#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number > 0:
    print(f"{number} is positve", end=' ')
elif (number == 0):
    print(f"{number} is zero", end=' ')
else:
    print(f"{number} is negative", end=' ')
