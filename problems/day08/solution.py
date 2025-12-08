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

    def __init__(self, box: Box | None = None) -> None:

        self.circuit_group = []

        if box is not None:
            self.size = 1
            self.circuit_group.append(box)
        else:
            self.size = 0

    def add_box(self, box: Box):
        self.circuit_group.append(box)
        self.size += 1
        return True

    def get_circuit_size(self):
        return self.size

    def get_circuit_full(self):
        return self.circuit_group

    def add_box_multiple(self, box_list: list):
        self.size += len(box_list)
        for box in box_list:
            self.circuit_group.append(box)
        return True

    def test_box(self, box: Box):
        if box in self.circuit_group:
            return True
        return False


def multiply_list(num_list: list[int]):
    output = 1
    for num in num_list:
        output *= num

    return output


def check_all_boxes(boxes: list[Box], circuit: Circuit):
    for box in boxes:
        if not circuit.test_box(box):
            return False

    return True


def solve_part2(text_in):
    boxes = get_boxes(text_in)
    distances = get_distances(boxes)
    sorted_distances = get_distances_sorted(distances)
    # print(f"Original len(sorted_distances): {len(sorted_distances)}")

    merging_pair_current = []
    pair_checked = []

    circuit_list: list[Circuit] = []
    while len(sorted_distances) > 0:
        item = sorted_distances.pop()
        junction_pair = item[0]

        updated_circuit_list = add_junction_pair_part1(circuit_list, junction_pair)
        circuit_list = updated_circuit_list
        # if key == 1:
        merging_pair_current = junction_pair
        pair_checked.append(merging_pair_current)

        if len(circuit_list) == 1:
            test_circuit = circuit_list[0]
            if check_all_boxes(boxes, test_circuit):
                pass
                # print(f"Current len(sorted_distances): {len(sorted_distances)}")
                # print(merging_pair_current)
                #
                break

    print(f"merging_pair_current: {merging_pair_current}")
    # for i in pair_checked:
    #     dist = get_distance(i[0], i[1])
    #     print(i, dist)

    answer = merging_pair_current[0].x * merging_pair_current[1].x
    return answer


def solve_part1(text_in):
    iterations = 1000
    mult_items = 3
    boxes = get_boxes(text_in)
    for box in boxes:
        print(box)

    distances = get_distances(boxes)
    sorted_distances = get_distances_sorted(distances)
    circuit_list: list[Circuit] = []
    for i in range(iterations):
        item = sorted_distances[i]

        junction_pair = item[0]

        updated_circuit_list = add_junction_pair_part1(circuit_list, junction_pair)
        circuit_list = updated_circuit_list

    size_list: list[int] = []
    for circuit in circuit_list:
        size_list.append(circuit.get_circuit_size())

    size_list.sort(reverse=True)
    print(size_list)

    output_number = multiply_list(size_list[:mult_items])

    return output_number


def merge_circuits(circuit_1: Circuit, circuit_2: Circuit) -> Circuit:
    output = Circuit()
    merged_circuit = circuit_1.get_circuit_full() + circuit_2.get_circuit_full()
    output.add_box_multiple(merged_circuit)
    return output


def add_junction_pair_part2(circuit_list: list[Circuit], junction_pair: list[Box]):
    # key = 1 if circuilist has a change
    key = 0

    box1 = junction_pair[0]
    box2 = junction_pair[1]
    output_circuit_list: list[Circuit] = []
    box1_circuit = None
    box2_circuit = None

    for circuit_item in circuit_list:

        if circuit_item.test_box(box1):
            box1_circuit = circuit_item
        if circuit_item.test_box(box2):
            box2_circuit = circuit_item

    if box1_circuit == box2_circuit:

        if (box1_circuit is not None) and (box2_circuit is not None):
            # box1 and box2 are both already in an item of circuit_list
            output_circuit_list = circuit_list
            return output_circuit_list, key

        if (box1_circuit is None) and (box2_circuit is None):
            # box1 and box2 both are not in any of the pre-existing circuits
            key = 1
            new_circuit = Circuit(box1)
            new_circuit.add_box(box2)
            output_circuit_list = circuit_list
            output_circuit_list.append(new_circuit)
            return output_circuit_list, key

    if box1_circuit != box2_circuit:
        output_circuit_list = circuit_list
        if (
            box2_circuit is None and box1_circuit is not None
        ):  # -> box1_circuit is not empty
            # box1 is present in a circuit and box2 is not present in any circuits
            # add box2 to box1_circuit, delete older instance of box1_circuit
            key = 1
            output_circuit_list.remove(box1_circuit)
            box1_circuit.add_box(box2)
            output_circuit_list.append(box1_circuit)
            return output_circuit_list, key

        if (
            box1_circuit is None and box2_circuit is not None
        ):  # -> box2_circuit is not empty
            # box2 is present in a circuit and box1 is not present in any circuits
            # add box1 to box2_circuit, delete older instance of box2_circuit
            key = 1
            output_circuit_list.remove(box2_circuit)
            box2_circuit.add_box(box1)
            output_circuit_list.append(box2_circuit)
            return output_circuit_list, key

        if (box1_circuit is not None) and (box2_circuit is not None):
            # box1 and box2 are present in different circiuits
            # remove box1_circuit and box2_circuit from output_circuit_list
            # add merged_circuit of box1_circuit and box2_circuit to output_circuit_list
            key = 1
            output_circuit_list.remove(box1_circuit)
            output_circuit_list.remove(box2_circuit)
            output_circuit_list.append(merge_circuits(box1_circuit, box2_circuit))
            return output_circuit_list, key

    # should not reach here
    print(f"Error in add_junction_pair")

    return [], key


def add_junction_pair_part1(circuit_list: list[Circuit], junction_pair: list[Box]):
    box1 = junction_pair[0]
    box2 = junction_pair[1]
    output_circuit_list: list[Circuit] = []
    box1_circuit = None
    box2_circuit = None

    for circuit_item in circuit_list:

        if circuit_item.test_box(box1):
            box1_circuit = circuit_item
        if circuit_item.test_box(box2):
            box2_circuit = circuit_item

    if box1_circuit == box2_circuit:

        if (box1_circuit is not None) and (box2_circuit is not None):
            # box1 and box2 are both already in an item of circuit_list
            output_circuit_list = circuit_list
            return output_circuit_list

        if (box1_circuit is None) and (box2_circuit is None):
            # box1 and box2 both are not in any of the pre-existing circuits
            new_circuit = Circuit(box1)
            new_circuit.add_box(box2)
            output_circuit_list = circuit_list
            output_circuit_list.append(new_circuit)
            return output_circuit_list

    if box1_circuit != box2_circuit:
        output_circuit_list = circuit_list
        if (
            box2_circuit is None and box1_circuit is not None
        ):  # -> box1_circuit is not empty
            # box1 is present in a circuit and box2 is not present in any circuits
            # add box2 to box1_circuit, delete older instance of box1_circuit
            output_circuit_list.remove(box1_circuit)
            box1_circuit.add_box(box2)
            output_circuit_list.append(box1_circuit)
            return output_circuit_list

        if (
            box1_circuit is None and box2_circuit is not None
        ):  # -> box2_circuit is not empty
            # box2 is present in a circuit and box1 is not present in any circuits
            # add box1 to box2_circuit, delete older instance of box2_circuit
            output_circuit_list.remove(box2_circuit)
            box2_circuit.add_box(box1)
            output_circuit_list.append(box2_circuit)
            return output_circuit_list

        if (box1_circuit is not None) and (box2_circuit is not None):
            # box1 and box2 are present in different circiuits
            # remove box1_circuit and box2_circuit from output_circuit_list
            # add merged_circuit of box1_circuit and box2_circuit to output_circuit_list
            output_circuit_list.remove(box1_circuit)
            output_circuit_list.remove(box2_circuit)
            output_circuit_list.append(merge_circuits(box1_circuit, box2_circuit))
            return output_circuit_list

    # should not reach here
    print(f"Error in add_junction_pair")

    return []


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
    return sorted(distances, key=lambda x: x[1], reverse=True)


def get_boxes(text_in):
    output = []
    for item in text_in:
        x, y, z = list(map(int, item.split(",")))
        output.append(Box(x, y, z))

    return output


@aoc_script
def main(file: str = ""):
    text_in = input_to_list(file)
    # print(text_in)
    # part1 = solve_part1(text_in)
    # print(f"part1: {part1}")
    part2 = solve_part2(text_in)
    print(f"part2: {part2}")


if __name__ == "__main__":
    main()
