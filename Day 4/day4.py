"""
Advent of Code 2019: Day 4
"""

from typing import List


def find_passwords(lower: int, upper: int) -> List[str]:
    possible_passwords: List[str] = []
    for password in range(lower, upper):
        password = str(password)

        two_adjacent = False
        adjacent_value = '0'
        previous_number = '0'

        # Check if it is a 6-digit number
        if len(password) != 6:
            print("length")
            continue

        for number in password:
            if previous_number == number:

                if two_adjacent and adjacent_value == number:
                    two_adjacent = False
                    continue

                elif not two_adjacent and adjacent_value == number:
                    continue

                two_adjacent = True
                adjacent_value = number

                """
                112233 meets these criteria because the digits never decrease and all repeated digits are exactly two digits long.
                123444 no longer meets the criteria (the repeated 44 is part of a larger group of 444).
                111122 meets the criteria (even though 1 is repeated more than twice, it still contains a double 22).
                """

            elif previous_number > number:
                break
            previous_number = number

        else:  # Exited naturally from inner for loop
            if two_adjacent:
                possible_passwords.append(password)

        continue  # Broken inside inner loop

    return possible_passwords


data_file = open("data.txt", "r")

lower_bound, upper_bound = map(int, data_file.readline().split("-"))

data_file.close()

passwords = find_passwords(lower_bound, upper_bound)

print("Number of passwords: {}".format(len(passwords)))
