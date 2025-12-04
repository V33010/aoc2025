import copy
import sys
from pathlib import Path
from typing import final

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from utils import aoc_script


def is_access_possible(arrangement, location):
    count = 0
    xloc, yloc = location
    xlen = len(arrangement)  # length in vertical direction
    ylen = len(arrangement[0])  # length in horizontal direction
    count_locs = []
    xtest, ytest = 0, 0
    test_locs = []

    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            xtest = xloc + i
            ytest = yloc + j
            test_locs.append((xtest, ytest))

    for loc in test_locs:
        xtest, ytest = loc
        if loc != location:
            if xtest >= 0 and ytest >= 0 and xtest < xlen and ytest < ylen:
                if arrangement[xtest][ytest] == "@":
                    count_locs.append((xtest, ytest))
                    count += 1

    # print(test_locs)
    # print(f"count: {count} at location: {count_locs}")
    # print(f"count_locs: {count_locs}")
    if count >= 4:
        return False

    return True


def solve_part1(text_in):
    total = 0
    xlen = len(text_in)
    ylen = len(text_in[0])
    print(f"xlen: {xlen}, ylen: {ylen}")
    for xloc in range(xlen):
        for yloc in range(ylen):
            location = xloc, yloc
            if text_in[xloc][yloc] == "@":
                print()
                print(f"'@' found at {location}")
                if is_access_possible(text_in, location):
                    print(f"location: {location} found accessible")
                    total += 1

    return total


def remove_once(arrangement):
    total = 0
    xlen = len(arrangement)
    ylen = len(arrangement[0])
    print(f"xlen: {xlen}, ylen: {ylen}")
    final_arrangement = copy.copy(arrangement)

    for xloc in range(xlen):
        for yloc in range(ylen):
            location = xloc, yloc
            if arrangement[xloc][yloc] == "@":
                # print()
                # print(f"'@' found at {location}")
                if is_access_possible(arrangement, location):
                    # print(f"location: {location} found accessible")
                    final_arrangement[xloc][yloc] = "."
                    total += 1

    return final_arrangement, total


def solve_part2(text_in):
    total_removed = 0
    arrangement = text_in
    removeable = 1
    iteration = 0

    while removeable != 0:
        iteration += 1
        final_arrangement, total = remove_once(arrangement)
        removeable = total
        arrangement = final_arrangement
        total_removed += total
        print(f"iteration: {iteration}, removed: {removeable}")

    return total_removed

    pass


def pretty_print_arrangement(text_in):
    print("  ", end="")
    for i in range(len(text_in)):
        print(i, end="")

    print()

    for i in range(len(text_in)):
        print(i, text_in[i])

    return 0


def input_to_list(file):
    output = []
    file = file.split("\n")
    for line in file:
        if line.strip() != "":
            output.append(list(line.strip()))
    return output


@aoc_script
def main(file: str = ""):
    text_in = input_to_list(file)
    pretty_print_arrangement(text_in)
    # part1 = solve_part1(text_in)
    # print(part1)
    part2 = solve_part2(text_in)
    print(part2)


if __name__ == "__main__":
    main()
