import sys
from itertools import permutations
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


def solve_part1(text_in):
    parsed_input = parse_input(text_in)
    total = 0
    for item in parsed_input:
        # print(item)
        light_diagram, wiring_schematics, joltage_requirement = item
        valid_buttons, len = run_system_part1(light_diagram, wiring_schematics)
        total += len

    return total

    pass


def toggle_bulb(bulb):
    if bulb == ".":
        return "#"
    else:
        return "."


def toggle_light(light_diagram, button):
    light_diagram_output = light_diagram
    for i in button:
        light_diagram_output[i] = toggle_bulb(light_diagram[i])

    return light_diagram_output


def toggle_light_multiple(light_size, buttons):
    light_diagram_output = ["."] * light_size
    for button in buttons:
        light_diagram_output = toggle_light(light_diagram_output, button)

    return light_diagram_output


def run_system_part1(correct_light_diagram, button_options):
    light_size = len(correct_light_diagram)
    iterations = len(button_options)
    valid_buttons = []
    for i in range(1, iterations + 1):
        possible_button_options = permutations(button_options, i)
        for test_buttons in possible_button_options:
            if correct_light_diagram == toggle_light_multiple(light_size, test_buttons):
                valid_buttons = test_buttons
                return valid_buttons, len(valid_buttons)

    # should never reach here
    print(f"Error in run_system_part1 for: {correct_light_diagram}")
    return []


def parse_row(row: str):
    # print()
    # print(row)
    row_split = row.split(" ")
    # print(f"row_split: {row_split}")

    light_diagram = row_split.pop(0)
    light_diagram = list(light_diagram[1 : len(light_diagram) - 1])
    # print(f"light_diagram: {light_diagram}")

    joltage_requirement = row_split.pop(-1)
    joltage_requirement = joltage_requirement[1 : len(joltage_requirement) - 1].split(
        ","
    )
    joltage_requirement = [int(item) for item in joltage_requirement]

    wiring_schematics = row_split
    wiring_schematics = [
        schematic[1 : len(schematic) - 1].split(",") for schematic in wiring_schematics
    ]
    wiring_schematics = [list(map(int, schematic)) for schematic in wiring_schematics]

    # print(f"wiring_schematics: {wiring_schematics}")
    # print(f"joltage_requirement: {joltage_requirement}")

    return light_diagram, wiring_schematics, joltage_requirement


def parse_input(text_in):
    output = []
    for row in text_in:
        output.append(parse_row(row))
    return output


@aoc_script
def main(file: str = ""):
    text_in = input_to_list(file)
    # print(text_in)
    part1 = solve_part1(text_in)
    print(f"part1: {part1}")


if __name__ == "__main__":
    main()
