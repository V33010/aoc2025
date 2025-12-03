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


def max_num_part1(num_str: str):
    max_num = 0
    for i in range(len(num_str) - 1):
        for j in range(i + 1, len(num_str)):
            current = num_str[i] + num_str[j]
            if int(current) > max_num:
                max_num = int(current)

    return max_num


def total_joltage_part1(text_in):
    sum = 0
    for bank in text_in:
        max_num = max_num_part1(bank)
        sum += int(max_num)

    return sum


def max_num_part2(num_str: str):
    max_num = 0
    n = len(num_str)
    start = 0
    digits_remaining = 12
    output = []

    while digits_remaining > 0:
        end = n - (digits_remaining - 1)
        window = num_str[start:end]
        best_digit = max(window)
        output.append(best_digit)

        first_occurence = num_str.index(best_digit, start, end)

        start = first_occurence + 1
        digits_remaining -= 1

    return "".join(output)


def total_joltage_part2(text_in):
    sum = 0
    for bank in text_in:
        max_num = max_num_part2(bank)
        sum += int(max_num)

    return sum


@aoc_script
def main(file: str = ""):
    text_in = input_to_list(file)
    # print(text_in)
    part1 = total_joltage_part1(text_in)
    print(f"part1: {part1}")
    part2 = total_joltage_part2(text_in)
    print(f"part2: {part2}")


if __name__ == "__main__":
    main()
