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


def get_points_integers(text_in):
    points = []
    for line in text_in:
        parts = list(map(int, line.split(",")))
        # keeping as tuple (x, y) for geometry logic
        points.append((parts[0], parts[1]))
    return points


def get_path_edges(points):
    edges_h = []
    edges_v = []
    n = len(points)

    for i in range(n):
        p1 = points[i]
        p2 = points[(i + 1) % n]

        if p1[0] == p2[0]:  # vertical edge
            # store: x, min_y, max_y
            edges_v.append([p1[0], min(p1[1], p2[1]), max(p1[1], p2[1])])
        else:  # horizontal edge
            # store: y, min_x, max_x
            edges_h.append([p1[1], min(p1[0], p2[0]), max(p1[0], p2[0])])

    return edges_h, edges_v


def get_all_candidates(points):
    candidates = []
    n = len(points)
    for i in range(n):
        for j in range(i + 1, n):
            p1 = points[i]
            p2 = points[j]

            width = abs(p1[0] - p2[0]) + 1
            height = abs(p1[1] - p2[1]) + 1
            area = width * height

            candidates.append([area, p1, p2])
    return candidates


def check_obstruction(p1, p2, edges_h, edges_v):
    min_x, max_x = min(p1[0], p2[0]), max(p1[0], p2[0])
    min_y, max_y = min(p1[1], p2[1]), max(p1[1], p2[1])

    # check horizontal edges
    for edge in edges_h:
        ey, ex1, ex2 = edge
        # if edge is strictly inside y range
        if min_y < ey < max_y:
            # And X ranges overlap
            if not (ex2 <= min_x or ex1 >= max_x):
                return True

    # check vertical edges
    for edge in edges_v:
        ex, ey1, ey2 = edge
        # if edge is strictly inside x range
        if min_x < ex < max_x:
            # And y ranges overlap
            if not (ey2 <= min_y or ey1 >= max_y):
                return True

    return False


def check_inside_loop(p1, p2, edges_v):
    min_x, max_x = min(p1[0], p2[0]), max(p1[0], p2[0])
    min_y, max_y = min(p1[1], p2[1]), max(p1[1], p2[1])

    # ray casting from the center point of the rectangle
    cx = (min_x + max_x) / 2
    cy = (min_y + max_y) / 2

    intersections = 0
    for edge in edges_v:
        ex, ey1, ey2 = edge
        # check if vertical edge straddles the ray Y
        if ey1 < cy < ey2:
            # check if edge is to the right
            if ex > cx:
                intersections += 1

    # odd intersections = inside, even intersections = outside
    return intersections % 2 == 1


def solve_part2(text_in):
    print("getting points integers")
    points = get_points_integers(text_in)

    print("getting path edges")
    edges_h, edges_v = get_path_edges(points)

    print("generating candidates")
    candidates = get_all_candidates(points)

    # check largest areas first
    candidates.sort(key=lambda x: x[0], reverse=True)

    print(f"checking {len(candidates)} candidates...")

    for item in candidates:
        area = item[0]
        p1 = item[1]
        p2 = item[2]

        # step 1: ensure no green path lines cut through the rectangle
        if check_obstruction(p1, p2, edges_h, edges_v):
            continue

        # step 2: ensure the rectangle is actually inside the loop (not outside)
        if check_inside_loop(p1, p2, edges_v):
            print(f"found valid max area: {area}")
            return area

    return 0


@aoc_script
def main(file: str = ""):
    text_in = input_to_list(file)
    # print(text_in)
    part2 = solve_part2(text_in)
    print(f"part2: {part2}")


if __name__ == "__main__":
    main()
