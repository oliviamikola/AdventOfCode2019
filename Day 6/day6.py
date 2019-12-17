"""
Advent of Code 2019: Day 5
"""

from typing import List, Dict, Set


class Orbit:
    """
    Represents an orbit
    """
    def __init__(self, name: str):
        self.name: str = name
        self.root: bool = True
        self.children: List[Orbit] = []

    def __str__(self) -> str:
        return_string = "{}: ".format(self.name)

        for child in self.children:
            return_string += child.name + ", "

        return return_string[: len(return_string) - 2]


def create_graph(open_file) -> Dict:
    """
    Creates the graph representing what orbits what
    :param open_file: file containing given data (assumed to be correct)
    :return: dictionary of orbits map
    """
    orbit_map = {}

    for orbit in open_file:
        left, right = orbit.strip().split(")")

        # Check if origin and orbiter are in the map already
        # Keys are strings, not Orbit objects
        if left not in orbit_map:
            orbit_map[left] = Orbit(left)
        if right not in orbit_map:
            orbit_map[right] = Orbit(right)

        orbit_map[right].root = False
        orbit_map[left].children.append(orbit_map[right])
        orbit_map[right].children.append(orbit_map[left])

    return orbit_map


def count_singular_orbits(seen_orbits: Set[str], orbit: Orbit, depth: int = 0):
    if orbit.name in seen_orbits:
        return 0
    seen_orbits.add(orbit.name)
    return depth + sum(count_singular_orbits(seen_orbits, child, depth + 1) for child in orbit.children)


def count_total_orbits(orbit_map: Dict):
    seen_orbits: Set[str] = set()
    # Need the orbit to be a root or it will be double counted
    return sum(count_singular_orbits(seen_orbits, orbit) for orbit in orbit_map.values() if orbit.root)


data_file = open("data.txt", "r")
orbits = create_graph(data_file)
data_file.close()

part1 = count_total_orbits(orbits)
part2 = 0

print("Part 1: {}".format(part1))
print("Part 2: {}".format(part2))
