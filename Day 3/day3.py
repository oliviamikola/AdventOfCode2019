"""
Advent of Code 2019: Day 3
"""

from typing import List, Dict


def calculate_points(wire: List[str]) -> Dict:
    x = y = manhattan_distance = 0  # Assume starting point is at (0, 0)
    points = {}

    directions = {"R": (1, 0), "L": (-1, 0), "U": (0, 1), "D": (0, -1)}

    for instruction in wire:
        delta_x, delta_y = directions[instruction[0]]

        for _ in range(int(instruction[1:])):
            x += delta_x
            y += delta_y
            manhattan_distance += 1

            points[(x, y)] = manhattan_distance

    return points


data_file = open("data.txt", "r")

wire1 = data_file.readline().split(",")
wire2 = data_file.readline().split(",")

data_file.close()

wire1_path: Dict = calculate_points(wire1)
wire2_path: Dict = calculate_points(wire2)


intersections = [point for point in wire1_path if point in wire2_path]

part1 = min(abs(x) + abs(y) for (x, y) in intersections)
part2 = min(wire1_path[point] + wire2_path[point] for point in intersections)

print("Part 1: {}".format(part1))
print("Part 2: {}".format(part2))
