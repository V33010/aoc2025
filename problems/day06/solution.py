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


def input_to_list_unsanitized(file):
    output = []
    file = file.split("\n")
    for line in file:
        if line.strip() != "":
            output.append(line)
    return output


def add_nums(num_list):
    total = 0
    for item in num_list:
        total += item

    return total


def multiply_nums(num_list):
    total = 1
    for item in num_list:
        total *= item

    return total


def get_num_list(num_str):
    num_list = []
    current_digit = ""
    next_digit = ""
    memory_num = ""
    for i in range(len(num_str) - 1):
        current_digit = num_str[i]
        next_digit = num_str[i + 1]
        # print(f"current: {current_digit}, next: {next_digit}")
        if (current_digit == " ") and (next_digit == " "):
            continue

        if (current_digit != " ") and (next_digit != " "):
            memory_num += current_digit

        elif (current_digit != " ") and (next_digit == " "):
            memory_num += current_digit
            num_list.append(memory_num)
            memory_num = ""

        elif (current_digit == " ") and (next_digit != " "):
            pass

    num_list.append(memory_num + next_digit)
    return num_list


def get_vertical_list_part1(num_lists):
    vertical = []
    total_horizontal = len(num_lists[0])
    total_vertical = len(num_lists)
    for j in range(total_horizontal):
        current_vertical = []
        for i in range(total_vertical):
            try:
                current_vertical.append(num_lists[i][j])
            except:
                print(f"i: {i}, total_horizontal: {total_horizontal}")
                print(f"j: {j}, total_vertical: {total_vertical}")
                sys.exit()

        vertical.append(current_vertical)

    return vertical


def calculate_once_part1(problem):
    operation = problem[-1]
    numbers = list(map(int, problem[: len(problem) - 1]))
    # print(f"problem: {problem}")
    # print(f"numbers: {numbers}")
    if operation == "+":
        # print(f"output: {add_nums(numbers)}")
        return add_nums(numbers)

    if operation == "*":
        # print(f"output: {multiply_nums(numbers)}")
        return multiply_nums(numbers)

    print(f"Sus problem")
    return False


def get_vertical_list_part2(num_lists):
    total_horizontal = len(num_lists[0])
    total_vertical = len(num_lists)
    # print(f"total_horizontal: {total_horizontal}")
    # print(f"total_vertical: {total_vertical}")
    vertical = []
    for i in range(total_horizontal):
        item = ""
        for j in range(total_vertical):
            item += num_lists[j][i]
        vertical.append(item)

    return vertical


def separate_problems(list_in):
    item_length = len(list_in[0])
    # print(f"item_length: {item_length}")
    space_item = " " * item_length
    # print(f"space_item: '{space_item}'")
    current_item = ""
    next_item = ""
    memory = []
    output = []

    # print("Starting loop...")
    for i in range(len(list_in) - 1):
        current_item = list_in[i]
        next_item = list_in[i + 1]
        # print(f"current_item: {current_item}")
        # print(f"next_item: {next_item}")
        if (current_item != space_item) and (next_item != space_item):
            memory.append(current_item)
            continue
        if (current_item != space_item) and (next_item == space_item):
            memory.append(current_item)
            output.append(memory)
            memory = []
            continue

    memory.append(next_item)
    output.append(memory)

    return output


def sanitize_item(item):
    output = item.strip("*").strip("+").strip()
    return output


def calculate_once_part2(problem):
    operator = ""
    for item in problem:
        if "+" in item:
            operator = "+"
            break
        elif "*" in item:
            operator = "*"
            break
        # else:
        #     sys.exit("Error in calculate_once_part2: operator not found")

    num_list = []
    for item in problem:
        num_list.append(sanitize_item(item))

    num_list = list(map(int, num_list))
    if operator == "+":
        return add_nums(num_list)
    elif operator == "*":
        return multiply_nums(num_list)

    print("Error in calculate_once_part2")
    return False


def solve_part2(text_in):
    total = 0
    vertical_list = get_vertical_list_part2(text_in)
    # print(vertical_list)
    problems = separate_problems(vertical_list)
    # print(f"problems: {problems}")
    for problem in problems:
        total += calculate_once_part2(problem)

    return total


def solve_part1(text_in):
    num_lists = []
    total = 0

    # ignore the last element full of symbols
    # for item in text_in[: (len(text_in) - 1)]:

    for item in text_in:
        num_lists.append(get_num_list(item))

    # for num_list in num_lists:
    #     print(num_list)

    vertical_list = get_vertical_list_part1(num_lists)
    # print(vertical_list)

    for item in vertical_list:
        total += calculate_once_part1(item)

    return total


@aoc_script
def main(file: str = ""):
    text_in = input_to_list(file)
    # print(text_in)
    part1 = solve_part1(text_in)
    print(f"part1: {part1}")
    text_in_unsanitized = input_to_list_unsanitized(file)
    # print(text_in_unsanitized)
    part2 = solve_part2(text_in_unsanitized)
    print(f"part2: {part2}")


if __name__ == "__main__":
    main()
