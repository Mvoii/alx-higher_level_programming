#!/usr/bin/python3
for num in range(100):
    if num != 99:
        print("{number:02d}".format(number=num), end=", ")
    else:
        print("{number:02d}".format(number=num), end="\n")
