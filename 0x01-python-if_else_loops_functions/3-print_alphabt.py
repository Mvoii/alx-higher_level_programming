#!/usr/bin/activate
for i in range(97, 123):
	if i != 101 and i != 113:
		print(f"{i}".format(character=chr(i)), end= " ")
