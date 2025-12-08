import math
import sys
from itertools import combinations
from pathlib import Path

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from utils import aoc_script


class Box:
    def __init__(self, x, y, z) -> None:
        self.x = x
        self.y = y
        self.z = z

    def __str__(self) -> str:
        return f"box position: {self.x}, {self.y}, {self.z}"

    def __repr__(self):
        return f"Box({self.x}, {self.y}, {self.z})"

    def get_position(self):
        position = [self.x, self.y, self.z]
        return position


class Circuit:
    circuit_chain = []

    def __init__(self, box: Box) -> None:
        self.start = box
        self.end = box
        self.size = 1
        self.circuit_chain.append(box)

    def add_box_end(self, box: Box):
        self.circuit_chain.append(box)
        self.end = box
        self.size += 1
        return True

    def add_box_start(self, box: Box):
        self.circuit_chain.insert(0, box)
        self.start = box
        self.size += 1
        return True

    def get_circuit_size(self):
        return self.size

    def get_circuit_full(self):
        return self.circuit_chain

    def get_endpoints(self):
        endpoints = [self.start, self.end]
        return endpoints


def add_junction_pair(circuit_list, junction: Box):
    # check circuit_list endpoints for TODO
    for circuit_item in circuit_list:
        endpoints = circuit_item.get_endpoints()
        pass


def get_distance(box1: Box, box2: Box):
    del_x = box2.x - box1.x
    del_y = box2.y - box1.y
    del_z = box2.z - box1.z
    dist_squared = (del_x**2) + (del_y**2) + (del_z**2)
    dist = math.sqrt(dist_squared)
    return dist


def input_to_list(file):
    output = []
    file = file.split("\n")
    for line in file:
        if line.strip() != "":
            output.append(line.strip())
    return output


def get_distances(boxes):
    distances = []
    box_combinations = list(combinations(boxes, 2))
    box_combination_list = [list(c) for c in box_combinations]
    for box_combination in box_combination_list:
        box1 = box_combination[0]
        box2 = box_combination[1]
        dist = get_distance(box1, box2)
        output = [[box1, box2], dist]
        distances.append(output)

    return distances


def get_distances_sorted(distances):
    return sorted(distances, key=lambda x: x[1])


def get_boxes(text_in):
    output = []
    for item in text_in:
        x, y, z = list(map(int, item.split(",")))
        output.append(Box(x, y, z))

    return output


def solve_part1(text_in):
    boxes = get_boxes(text_in)
    for box in boxes:
        print(box)

    distances = get_distances(boxes)
    sorted_distances = get_distances_sorted(distances)
    for distance in sorted_distances:
        print(distance)


@aoc_script
def main(file: str = ""):
    text_in = input_to_list(file)
    print(text_in)
    part1 = solve_part1(text_in)
    print(f"part1: {part1}")


if __name__ == "__main__":
    main()
