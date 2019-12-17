"""
Advent of Code 2019: Day 4
"""

from typing import List
import itertools


def find_passwords(lower: int, upper: int) -> List[str]:
    possible_passwords: List[str] = []
    for password in range(lower, upper):
        password = str(password)

        two_adjacent = False
        previous_number = '0'

        # Check if it is a 6-digit number
        if len(password) != 6:
            continue

        for number in password:
            if previous_number > number:  # Not in increasing order, ASCII comparisons
                break

            # Next two lines are for part 1
            elif previous_number == number:
                two_adjacent = True

            previous_number = number

        else:  # Exited naturally from inner for loop

            # The next 4 lines are fro part 2
            groups = [list(j) for i, j in itertools.groupby(password)]
            for group in groups:
                if len(group) == 2:
                    two_adjacent = True

            if two_adjacent:
                possible_passwords.append(password)

        continue  # Broken in inner loop

    return possible_passwords


data_file = open("data.txt", "r")

lower_bound, upper_bound = map(int, data_file.readline().split("-"))

data_file.close()

passwords = find_passwords(lower_bound, upper_bound)

print("Number of passwords: {}".format(len(passwords)))
