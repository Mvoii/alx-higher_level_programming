#!/usr/bin/python3
for first_digit in range(10):
    for second_digit in range(10):
        if first_digit == 8 and second_digit == 9:
            print("{one}{two}".format(one=first_digit,
                                      two=second_digit), end="\n")
        elif first_digit < second_digit and first_digit != second_digit:
            print("{one}{two}".format(one=first_digit,
                                      two=second_digit), end=", ")
