import sys
from pathlib import Path

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from utils import aoc_script


def pretty_print(system):
    for row in system:
        print(row)

    return 0


def input_to_list(file):
    output = []
    file = file.split("\n")
    for line in file:
        if line.strip() != "":
            output.append(line.strip())
    return output


def find_system_params(setup: list):
    start_row = setup[0]
    loc_start = start_row.index("S")
    system_width = len(setup[0])
    system_length = len(setup)

    return loc_start, system_width, system_length


def progress_for_splitter(initial_row, splitter_row, system_width):
    split_count = 0
    output_row = [None] * system_width
    if initial_row[0] == 1:
        output_row[0] = 1

    if initial_row[-1] == 1:
        output_row[-1] = 1

    for i in range(1, system_width - 1):
        if (initial_row[i] == 1) and (splitter_row[i] == "^"):
            try:
                split_count += 1
                output_row[i - 1] = 1
                output_row[i + 1] = 1
            except IndexError:
                print(f"IndexError at i: {i}, len(output_row): {len(output_row)}")

        elif (initial_row[i] == 1) and (splitter_row[i] == "."):
            output_row[i] = 1

    return output_row, split_count


def progress_for_normal(initial_row, normal_row, system_width):
    return initial_row, 0


def run_system(system):
    total_split_count = 0
    loc_start, system_width, system_length = find_system_params(system)
    initial_row = [0] * system_width
    initial_row[loc_start] = 1
    for i in range(1, len(system)):
        split_count = 0
        obstacle_row = system[i]
        output_row = []
        if "^" in obstacle_row:
            output_row, split_count = progress_for_splitter(
                initial_row, obstacle_row, system_width
            )

        else:
            output_row, split_count = progress_for_normal(
                initial_row, obstacle_row, system_width
            )

        total_split_count += split_count

        initial_row = output_row

    return total_split_count


def solve_part1(text_in):
    total_split_count = run_system(text_in)
    return total_split_count


@aoc_script
def main(file: str = ""):
    text_in = input_to_list(file)
    # print(text_in)
    # pretty_print(text_in)
    part1 = solve_part1(text_in)
    print(f"part1: {part1}")


if __name__ == "__main__":
    main()
