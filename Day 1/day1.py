"""
Advent of Code 2019: Day 1
"""

import math


def calculate_fuel(mass: int):
    fuel: int = 0
    while True:
        required_fuel = math.floor(mass / 3) - 2

        if required_fuel <= 0:
            return fuel
        else:
            fuel += required_fuel
            mass = required_fuel


data_file = open("data.txt", "r")

total_fuel: int = 0

for mass_str in data_file:
    total_fuel += calculate_fuel(int(mass_str))

print(total_fuel)

data_file.close()
