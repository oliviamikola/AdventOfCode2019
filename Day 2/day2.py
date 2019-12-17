"""
Advent of Code 2019: Day 2
"""

from typing import List
from copy import deepcopy


def calculate(code: List[int], noun: int, verb: int) -> int:
    code[1] = noun
    code[2] = verb

    current_index = 0
    indices = len(code)

    while current_index < indices:
        opcode = code[current_index]

        first_input = code[code[current_index + 1]]
        second_input = code[code[current_index + 2]]
        position = code[current_index + 3]

        if opcode == 1:  # Add
            add = first_input + second_input
            # print("Addition: {} + {} = {} at {}".format(first_input, second_input, add, position))
            code[position] = add

        elif opcode == 2:  # Multiply
            mult = first_input * second_input
            # print("Multiplication: {} * {} = {} at {}".format(first_input, second_input, mult, position))
            code[position] = mult

        elif opcode == 99:  # Halt
            # print("Halt")
            break

        else:
            print("Something went wrong")
            break

        current_index += 4

    return code[0]


data_file = open("data.txt", "r")

data = data_file.readline()
data = list(map(int, data.strip().split(",")))

data_file.close()

# replace position 1 with the value 12 and replace position 2 with the value 2
part1 = calculate(deepcopy(data), 1, 12)
print("Part 1: {}".format(part1))

for noun in range(100):
    for verb in range(100):
        output = calculate(deepcopy(data), noun, verb)
        if output == 19690720:
            part2 = 100 * noun + verb
            print("Part 2: {}".format(part2))
            break

    else:
        continue  # Exited naturally from inner for loop

    break  # Broken inside inner loop
