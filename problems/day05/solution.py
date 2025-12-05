import sys
from os import truncate
from pathlib import Path

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from utils import aoc_script


def input_to_list(file):
    output_ranges = []
    output_ingredients = []
    temp = []
    file = file.split("\n")
    for line in file:
        if line.strip() != "":
            temp.append(line.strip())

    index = 0
    key = "range"
    while key == "range":
        if "-" not in temp[index]:
            key = "ingredient"
            break
        output_ranges.append(temp[index])
        index += 1

    while index < len(temp):
        output_ingredients.append(temp[index])
        index += 1

    return output_ranges, output_ingredients


def is_in_range(given_range, ingredient):
    rangeL, rangeR = list(map(int, given_range.split("-")))
    ingredient = int(ingredient)
    if (ingredient >= rangeL) and (ingredient <= rangeR):
        return True

    return False


def solve_part1(ranges, ingredients):
    count = 0
    checked = []
    for given_range in ranges:
        for ingredient in ingredients:
            if is_in_range(given_range, ingredient) and (ingredient not in checked):
                # print(f"ingredient: {ingredient} lies in given_range: {given_range}")
                count += 1
                checked.append(ingredient)

    return count


def convert_ranges(ranges):
    output = []
    for given_range in ranges:
        l, r = list(map(int, given_range.split("-")))
        output.append([l, r])

    output.sort()
    return output


def merge_ranges(ranges):
    merged_ranges = []
    current_range = ranges[0]
    for i in range(1, len(ranges)):
        next_range = ranges[i]
        if next_range[0] <= current_range[1] + 1:
            merged = [current_range[0], max(next_range[1], current_range[1])]
            current_range = merged

        else:
            merged_ranges.append(current_range)
            current_range = next_range

    merged_ranges.append(current_range)

    return merged_ranges


def count_all(merged_ranges):
    count = 0
    for range_item in merged_ranges:
        L, R = range_item[0], range_item[1]
        count += R - L + 1

    return count


def find_all_ingredients(given_range):
    ingredients_list = []
    rangeL, rangeR = list(map(int, given_range.split("-")))
    for i in range(rangeL, rangeR + 1):
        ingredients_list.append(i)
    return ingredients_list


def solve_part2(ranges):
    converted_ranges = convert_ranges(ranges)
    merged_ranges = merge_ranges(converted_ranges)
    count = count_all(merged_ranges)
    return count


@aoc_script
def main(file: str = ""):
    output_ranges, output_ingredients = input_to_list(file)
    # print(f"output_ranges: {output_ranges}")
    # print(f"output_ingredients: {output_ingredients}")
    part1 = solve_part1(output_ranges, output_ingredients)
    part2 = solve_part2(output_ranges)
    print(f"part2: {part2}")


if __name__ == "__main__":
    main()
