import sys
from pathlib import Path

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from utils import aoc_script


def input_to_list(file):
    output = []
    file = file.split("\n")
    for line in file:
        if line.strip() != "":
            output.append(line.strip())

    output = output[0].split(",")

    return output


def check_symmetric_part1(num_str: str):
    if len(num_str) % 2 != 0:
        return False

    lhalf = num_str[: len(num_str) // 2]
    rhalf = num_str[len(num_str) // 2 :]

    if lhalf == rhalf:
        return True

    return False


def find_sum_part1(item):
    total = 0
    l_range = int(item.split("-")[0])
    r_range = int(item.split("-")[1])
    print(f"l_range: {l_range}")
    print(f"r_range: {r_range}")

    for i in range(l_range, r_range + 1):
        if check_symmetric_part1(str(i)):
            total += i

    return total


def solve_part1(text_in):
    full_sum = 0
    for item in text_in:
        full_sum += find_sum_part1(item)

    return full_sum


def check_symmetric_part2(num_str: str):
    repeat_counts = [7, 5, 3, 2]

    for count in repeat_counts:
        if len(num_str) % count == 0:
            slicer = len(num_str) // count
            control = num_str[:slicer]

            # Check all slices are identical
            for i in range(count):
                segment = num_str[i * slicer : (i + 1) * slicer]
                if segment != control:
                    break
            else:
                # Matched all segments
                print(f"num_str found correct: {num_str}")
                return True

    return False


def find_sum_part2(item):
    total = 0
    l_range = int(item.split("-")[0])
    r_range = int(item.split("-")[1])
    print(f"l_range: {l_range}")
    print(f"r_range: {r_range}")

    for i in range(l_range, r_range + 1):
        if check_symmetric_part2(str(i)):
            total += i

    return total


def solve_part2(text_in):
    full_sum = 0
    for item in text_in:
        full_sum += find_sum_part2(item)

    return full_sum


@aoc_script
def main(file: str = ""):
    text_in = input_to_list(file)
    part1_solution = solve_part1(text_in)
    # print(f"part1_solution: {part1_solution}")
    part2_solution = solve_part2(text_in)
    print(f"part2_solution: {part2_solution}")


if __name__ == "__main__":
    main()
