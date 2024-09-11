#!/usr/bin/python3
for a in range(26):
    letter = chr(122 - a) if a % 2 == 0 else chr(122 - a - 32)
    print("{}".format(letter), end="")
