# part 2: 6646 -> too high
# part 2: 6370 -> too low
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


def parse_item(item):
    if item[0] == "L":
        try:
            item_num = int(item[1:])
            return -1 * item_num
        except:
            print("Error in parsing:", item)
            pass

    elif item[0] == "R":
        try:
            item_num = int(item[1:])
            return item_num
        except:
            print("Error in parsing:", item)
            pass


def convert_item_list(text_in: list) -> list:
    output_list = [parse_item(i) for i in text_in]
    return output_list


def run_sequence_part1(list_in: list) -> int:
    counter = 0
    pointer = 50
    for item in list_in:
        print(f"pointer position at: {pointer}")

        pointer = pointer + item
        pointer = (pointer) % 100

        if pointer == 0:
            counter += 1

    return counter


def run_sequence_part2(list_in: list):
    counter = 0
    pointer = 50
    i = 0

    for item in list_in:

        if item > 0:
            for _ in range(item):
                pointer = (pointer + 1) % 100
                if pointer == 0:
                    counter += 1
        if item < 0:
            for _ in range(abs(item)):
                pointer = (pointer - 1) % 100
                if pointer == 0:
                    counter += 1

    return counter


@aoc_script
def main(file: str = ""):
    text_in = input_to_list(file)
    print("Starting solution...")
    print("text_in:", text_in)
    converted_item_list = convert_item_list(text_in)
    print("converted_item_list:", converted_item_list)
    password = run_sequence_part2(converted_item_list)
    print(f"Total items: {len(converted_item_list)}")
    print(f"password: {password}")


if __name__ == "__main__":
    main()
