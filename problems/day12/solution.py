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
    return output


def parse_input(text_in):
    areas = []
    shapes = []
    for i in range(len(text_in)):
        if "x" in text_in[i]:
            area_item = text_in[i]
            # areas.append(text_in[i])
            area_item = area_item.split(": ")
            size = list(map(int, area_item[0].split("x")))
            nums = list(map(int, (area_item[1].split(" "))))
            area = [size, nums]
            areas.append(area)

        elif "#" in text_in[i]:
            continue

        else:
            shape = []
            shape.append(int(text_in[i].strip(":")))
            shape.append(text_in[i + 1])
            shape.append(text_in[i + 2])
            shape.append(text_in[i + 3])
            shapes.append(shape)

    return shapes, areas


def check_area(area_item):
    size, num_list = area_item
    l, w = size
    max_area = l * w
    min_space_needed = 9 * sum(num_list)
    if min_space_needed > max_area:
        return False

    return True


def solve_part1(text_in):
    valids = 0
    shapes, areas = parse_input(text_in)
    # print(shapes)
    # print(areas)
    for item in areas:
        if check_area(item):
            valids += 1
    return valids


@aoc_script
def main(file: str = ""):
    text_in = input_to_list(file)
    print(text_in)
    print()
    part1 = solve_part1(text_in)
    print(f"part1: {part1}")


if __name__ == "__main__":
    main()
