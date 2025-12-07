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
            output.append(list(line.strip()))
    return output


def find_system_params(setup: list):
    start_row = setup[0]
    loc_start = start_row.index("S")
    system_width = len(setup[0])
    system_length = len(setup)

    return loc_start, system_width, system_length


def progress_for_splitter(initial_row, splitter_row, system_width):
    split_count = 0
    output_row = ["."] * system_width
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


def progress_for_splitter_right(initial_row, splitter_row, system_width):
    split_count = 0
    output_row = ["."] * system_width
    if initial_row[0] == 1:
        output_row[0] = 1

    if initial_row[-1] == 1:
        output_row[-1] = 1

    for i in range(1, system_width - 1):
        if (initial_row[i] == 1) and (splitter_row[i] == "^"):
            try:
                split_count += 1
                output_row[i + 1] = 1
            except IndexError:
                print(f"IndexError at i: {i}, len(output_row): {len(output_row)}")

        elif (initial_row[i] == 1) and (splitter_row[i] == "."):
            output_row[i] = 1

    return output_row  # , split_count


def progress_for_splitter_left(initial_row, splitter_row, system_width):
    split_count = 0
    output_row = ["."] * system_width
    if initial_row[0] == 1:
        output_row[0] = 1

    if initial_row[-1] == 1:
        output_row[-1] = 1

    for i in range(1, system_width - 1):
        if (initial_row[i] == 1) and (splitter_row[i] == "^"):
            try:
                split_count += 1
                output_row[i - 1] = 1
            except IndexError:
                print(f"IndexError at i: {i}, len(output_row): {len(output_row)}")

        elif (initial_row[i] == 1) and (splitter_row[i] == "."):
            output_row[i] = 1

    return output_row  # , split_count


def progress_for_normal(initial_row, normal_row, system_width):
    return initial_row, 0


def run_system_part1(system):
    total_split_count = 0
    loc_start, system_width, _ = find_system_params(system)
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
    total_split_count = run_system_part1(text_in)
    return total_split_count


def solve_part2(text_in):
    total_world_count = run_system_part2(text_in)
    return total_world_count


def split_worlds(world_in):

    light_row = world_in[0]
    obstacle_row = world_in[1]
    remaining_world = world_in[2:]

    if "^" not in obstacle_row:
        return "no_split", [light_row] + remaining_world

    else:
        light_loc = light_row.index(1)
        if obstacle_row[light_loc] == "^":
            output_row_left = progress_for_splitter_left(
                light_row, obstacle_row, len(world_in[0])
            )
            output_row_right = progress_for_splitter_right(
                light_row, obstacle_row, len(world_in[0])
            )

            split_world_left = [output_row_left] + remaining_world
            split_world_right = [output_row_right] + remaining_world

            return ("split", split_world_left, split_world_right)

        else:
            return "no_split", [light_row] + remaining_world


def run_system_part2(text_in):
    initial_world = text_in
    loc_start, system_width, system_length = find_system_params(initial_world)
    print(
        f"loc_start: {loc_start}, system_width: {system_width}, system_length: {system_length}"
    )
    initial_world[0][loc_start] = 1
    # pretty_print(initial_world)

    world_count = 0
    world_queue = [initial_world]
    while len(world_queue) > 0:
        print(f"worlds in world_queue: {len(world_queue)}")
        print(f"world_count: {world_count}")
        world = world_queue.pop()
        if len(world) == 1:
            # print(f"world: {world}")
            world_count += 1
            continue

        else:
            updated_output = split_worlds(world)
            if updated_output[0] == "no_split":
                updated_world = updated_output[1]
                world_queue.append(updated_world)
                continue
            if updated_output[0] == "split":
                updated_world_left = updated_output[1]
                updated_world_right = updated_output[2]
                world_queue.append(updated_world_left)
                world_queue.append(updated_world_right)
                continue

    return world_count


@aoc_script
def main(file: str = ""):
    text_in = input_to_list(file)
    # print(text_in)
    # pretty_print(text_in)
    # part1 = solve_part1(text_in)
    # print(f"part1: {part1}")
    part2 = solve_part2(text_in)
    print(f"part2: {part2}")


if __name__ == "__main__":
    main()
