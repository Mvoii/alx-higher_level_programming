#!/usr/bin/python3
for num in range(0, 99):
    print("{num} = {hex_num}".format(num=int(num), hex_num=hex(num)), end="\n")
