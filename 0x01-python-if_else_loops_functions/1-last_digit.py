#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = abs(number) % 10
order_range = ""

if (last_digit > 5 and number > 0):
    order_range = "greater than 5"
    print(f"Last digit of {number} is {last_digit} and is {order_range}")
elif (last_digit == 0):
    order_range = "0"
    print(f"Last digit of {number} is {last_digit} and is {order_range}")
else:
    if number < 0:
        last_digit = -last_digit
    order_range = "less than 6 and not 0"
    print(f"Last digit of {number} is {last_digit} and is {order_range}")
