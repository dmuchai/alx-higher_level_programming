#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return (0)
    roman_nums = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
    }
    total = 0
    previous_value = 0

    for letter in reversed(roman_string):
        int_value = roman_nums.get(letter, 0)

        if int_value < previous_value:
            total -= int_value
        else:
            total += int_value

        previous_value = int_value

    return total
