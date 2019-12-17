"""
Advent of Code 2019: Day 5
"""

from typing import List
from copy import deepcopy


def calculate(code: List[str]) -> int:
    current_index = 0
    count = 0

    while True:
        instruction = code[current_index]
        count += 1

        if len(instruction) < 5:
            instruction = '0'*(5 - len(instruction)) + instruction

        opcode = int(instruction[-2] + instruction[-1])
        first_mode = int(instruction[-3])
        second_mode = int(instruction[-4])

        if opcode == 1:  # Add
            first_input = int(code[current_index + 1])
            if first_mode == 0:
                first_input = code[int(code[current_index + 1])]

            second_input = int(code[current_index + 2])
            if second_mode == 0:
                second_input = code[int(code[current_index + 2])]

            code[int(code[current_index + 3])] = str(int(first_input) + int(second_input))
            current_index += 4

        elif opcode == 2:  # Multiply
            first_input = int(code[current_index + 1])
            if first_mode == 0:
                first_input = code[int(code[current_index + 1])]

            second_input = int(code[current_index + 2])
            if second_mode == 0:
                second_input = code[int(code[current_index + 2])]

            code[int(code[current_index + 3])] = str(int(first_input) * int(second_input))
            current_index += 4

        elif opcode == 3:
            code[int(code[current_index + 1])] = input("Enter System ID: ")
            current_index += 2

        elif opcode == 4:
            first_input = int(code[current_index + 1])
            if first_mode == 0:
                first_input = int(code[int(code[current_index + 1])])

            print(first_input)
            current_index += 2

        elif opcode == 5:  # jump-if-true
            first_input = int(code[current_index + 1])
            if first_mode == 0:
                first_input = int(code[int(code[current_index + 1])])

            second_input = int(code[current_index + 2])
            if second_mode == 0:
                second_input = int(code[int(code[current_index + 2])])

            if first_input != 0:
                current_index = second_input
            else:
                current_index += 3

        elif opcode == 6:  # jump-if-false
            first_input = int(code[current_index + 1])
            if first_mode == 0:
                first_input = int(code[int(code[current_index + 1])])

            second_input = int(code[current_index + 2])
            if second_mode == 0:
                second_input = int(code[int(code[current_index + 2])])

            if first_input == 0:
                current_index = second_input
            else:
                current_index += 3

        elif opcode == 7:  # Less than
            first_input = int(code[current_index + 1])
            if first_mode == 0:
                first_input = int(code[int(code[current_index + 1])])

            second_input = int(code[current_index + 2])
            if second_mode == 0:
                second_input = int(code[int(code[current_index + 2])])

            if first_input < second_input:
                code[int(code[current_index + 3])] = '1'
            else:
                code[int(code[current_index + 3])] = '0'

            current_index += 4

        elif opcode == 8:  # Equals
            first_input = int(code[current_index + 1])
            if first_mode == 0:
                first_input = int(code[int(code[current_index + 1])])

            second_input = int(code[current_index + 2])
            if second_mode == 0:
                second_input = int(code[int(code[current_index + 2])])

            if first_input == second_input:
                code[int(code[current_index + 3])] = '1'
            else:
                code[int(code[current_index + 3])] = '0'

            current_index += 4

        elif opcode == 99:  # Halt
            # print("Halt")
            print(code[current_index - 1])
            print(code[current_index + 1])
            break

        else:
            print(current_index)
            print(opcode)
            print(count)
            print("Something went wrong")
            break

    return int(code[0])


data_file = open("data.txt", "r")

data = data_file.readline()
# data = list(map(int, data.strip().split(",")))
data = data.strip().split(",")


data_file.close()

# replace position 1 with the value 12 and replace position 2 with the value 2
part1 = calculate(deepcopy(data))
print("Part 1: {}".format(part1))
