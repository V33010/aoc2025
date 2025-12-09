import sys
from itertools import combinations
from pathlib import Path

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from utils import aoc_script


def get_text_in_numbers(text_in):
    output = []
    for item in text_in:
        item = list(map(int, item.split(",")))
        item.reverse()
        output.append(item)

    # print(output)

    return output


def get_included_items(loc1, loc2):
    loc1_x, loc1_y = loc1
    loc2_x, loc2_y = loc2
    included_items = []
    if (loc1_x != loc2_x) and (loc1_y != loc2_y):
        print(f"improper slope for {loc1} and {loc2}")
        return []

    if (loc1_x == loc2_x) and (loc1_y == loc2_y):
        print(f"same points found: {loc1}, {loc2}")
        return loc1

    if (loc1_x == loc2_x) and (loc1_y != loc2_y):
        if loc2_y > loc1_y:
            for i in range(loc1_y, loc2_y + 1):
                included_items.append([loc1_x, i])
            return included_items
        else:
            for i in range(loc2_y, loc1_y + 1):
                included_items.append([loc1_x, i])
            return included_items

    if (loc1_x != loc2_x) and (loc1_y == loc2_y):
        if loc2_x > loc1_x:
            for i in range(loc1_x, loc2_x + 1):
                included_items.append([i, loc1_y])
            return included_items
        else:
            for i in range(loc2_x, loc1_x + 1):
                included_items.append([i, loc1_y])
            return included_items

    # should not reach here
    print(f"Error in get_included_items for locs: {loc1}, {loc2}")
    return []


def get_path_locs(text_in_numbers):
    numbers = text_in_numbers[:]
    temp = numbers[0]
    numbers.append(temp)
    path_locs = []
    for i in range(len(numbers) - 1):
        loc1 = numbers[i]
        loc2 = numbers[i + 1]
        included_items = get_included_items(loc1, loc2)
        path_locs = path_locs + included_items

    return path_locs


def flood_fill(boundary_tiles, surround_rectangle_tiles):

    start = surround_rectangle_tiles[0]
    island: list = surround_rectangle_tiles[:]
    queue = [start]
    while len(queue) > 0:
        current = queue.pop()
        current_x = current[0]
        current_y = current[1]
        loc_up = [current_x - 1, current_y]
        loc_down = [current_x + 1, current_y]
        loc_right = [current_x, current_y + 1]
        loc_left = [current_x, current_y - 1]
        available_locs = [loc_up, loc_down, loc_left, loc_right]
        if current in island:
            island.remove(current)
        for loc in available_locs:
            if loc in island and loc not in boundary_tiles:
                queue.append(loc)

    return island


def get_min_max_locs(tiles):
    x_locs = []
    y_locs = []
    for tile in tiles:
        x_locs.append(tile[0])
        y_locs.append(tile[1])

    x_locs = sorted(x_locs)
    y_locs = sorted(y_locs)
    min_x = x_locs[0]
    min_y = y_locs[0]
    max_x = x_locs[-1]
    max_y = y_locs[-1]
    return [min_x, max_x, min_y, max_y]


def get_surround_rectangle(text_in_numbers):
    x_locs = []
    y_locs = []
    for item in text_in_numbers:
        x_locs.append(item[0])
        y_locs.append(item[1])

    x_locs = sorted(x_locs)
    y_locs = sorted(y_locs)
    min_x = x_locs[0]
    min_y = y_locs[0]
    max_x = x_locs[-1]
    max_y = y_locs[-1]
    print(min_x, max_x)
    print(min_y, max_y)
    surround = []
    for i in range(min_x - 2, max_x + 3):
        print(f"i: {i}")
        for j in range(min_y - 2, max_y + 3):
            surround.append([i, j])

    return surround


def get_all_rectangle_tiles(rectangle):
    all_tiles = []
    start_x = 0
    start_y = 0
    end_x = 0
    end_y = 0
    p1_x, p1_y = list(map(int, rectangle[0].split(",")))
    p2_x, p2_y = list(map(int, rectangle[1].split(",")))

    if p2_x > p1_x:
        end_x = p2_x
        start_x = p1_x
    else:
        end_x = p1_x
        start_x = p2_x

    if p2_y > p1_y:
        end_y = p2_y
        start_y = p1_y
    else:
        end_y = p1_y
        start_y = p2_y

    for x in range(start_x, end_x + 1):
        for y in range(start_y, end_y + 1):
            all_tiles.append([x, y])

    return all_tiles


def check_rectangle(rectangle, island):
    all_rectangle_tiles = get_all_rectangle_tiles(rectangle)
    for tile in all_rectangle_tiles:
        tile.reverse()
        if tile not in island:
            print(f"tile: {tile} not in island")
            return False
    return True


def solve_part2(text_in):
    max = 0
    print("getting text_in_numbers")
    text_in_numbers = get_text_in_numbers(text_in)
    print("text_in_numbers received")
    # print(f"text_in_numbers: {text_in_numbers}")
    print("\ngetting path_locs")
    path_locs = get_path_locs(text_in_numbers)
    # for item in path_locs:
    #     print(item)
    print("path_locs received\n")
    print("getting surround_rectangle_tiles")
    surround_rectangle_tiles = get_surround_rectangle(text_in_numbers)
    # for tile in surround_rectangle_tiles:
    #     print(tile)
    #
    print("surround_rectangle_tiles received\n")
    print("starting flood_fill")
    island = flood_fill(path_locs, surround_rectangle_tiles)
    print("flood_fill completed")
    # for item in island:
    #     print(item)

    print(f"len(island): {len(island)}")
    all_rectangles = get_all_rectangles(text_in)
    for rectangle in all_rectangles:
        if check_rectangle(rectangle, island):
            area = get_area_once(rectangle[0], rectangle[1])
            print(f"area: {area}")
            if area > max:
                max = area

    return max


def get_all_rectangles(text_in):
    all_rectangles = list(combinations(text_in, 2))
    return all_rectangles


def get_all_areas(all_rectangles):
    output = []
    for item in all_rectangles:
        p1 = item[0]
        p2 = item[1]
        area = get_area_once(p1, p2)
        to_append = [p1, p2, area]
        output.append(to_append)

    return output


def get_area_once(p1, p2):
    p1_x, p1_y = list(map(int, p1.split(",")))
    p2_x, p2_y = list(map(int, p2.split(",")))
    # print(f"r1_x: {p1_x}, r1_y: {p1_y}")
    # print(f"r2_x: {p2_x}, r2_y: {p2_y}")

    # ignore below condition since equal x or y coordinate still has thickness 1
    # if (p1_x == p2_x) or (p1_y == p2_y):
    #     return 0

    len_x = 0
    len_y = 0
    if p2_x > p1_x:
        len_x = p2_x - p1_x + 1
        if p2_y > p1_y:
            len_y = p2_y - p1_y + 1
        else:
            len_y = p1_y - p2_y + 1

    else:
        len_x = p1_x - p2_x + 1
        if p2_y > p1_y:
            len_y = p2_y - p1_y + 1
        else:
            len_y = p1_y - p2_y + 1

    if len_x == 0 or len_y == 0:
        print(f"Error in getting area for p1: {p1}, p2: {p2}")
        return 0

    return len_x * len_y


def sort_areas(all_rectangles_with_area):
    return sorted(all_rectangles_with_area, key=lambda x: x[2])


def solve_part1(text_in):
    all_rectangles = get_all_rectangles(text_in)
    # print(all_rectangles)
    all_rectangles_with_area = get_all_areas(all_rectangles)
    # print(all_rectangles_with_area)
    sorted_areas = sort_areas(all_rectangles_with_area)
    # for item in sorted_areas:
    #     print(item)

    max_area = sorted_areas[-1][2]
    return max_area


def input_to_list(file):
    output = []
    file = file.split("\n")
    for line in file:
        if line.strip() != "":
            output.append(line.strip())
    return output


@aoc_script
def main(file: str = ""):
    text_in = input_to_list(file)
    # print(text_in)
    # part1 = solve_part1(text_in)
    # print(f"part1: {part1}")
    part2 = solve_part2(text_in)
    print(f"part2: {part2}")


if __name__ == "__main__":
    main()
