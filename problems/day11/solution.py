import sys
from copy import copy
from pathlib import Path

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from utils import aoc_script


class Node:
    def __init__(self, self_name, children_names):
        self.self_name = self_name
        self.children_names = children_names
        self.next_exists = False if "out" in children_names else True

    def __str__(self) -> str:
        return f"self_name: {self.self_name}, children_names: {self.children_names}, next_exists: {self.next_exists}"

    def __repr__(self) -> str:
        return f"Node({self.self_name})"


def input_to_list(file):
    output = []
    file = file.split("\n")
    for line in file:
        if line.strip() != "":
            output.append(line.strip())
    return output


class DevicePath:
    def __init__(self, node: Node):

        self.path = [node]

        self.head = node
        self.tail = node

    def __str__(self):
        output = ""
        for node_item in self.path:
            output += str(node_item.self_name) + " "
        return output

    def add_node(self, new_node: Node):
        self.path.append(new_node)
        self.tail = new_node

    def test_node(self, node: Node):
        if node in self.path:
            return True
        return False


def test_paths(paths):
    for path in paths:
        tail_name = path.tail.self_name
        if tail_name != "you":
            return False

    return True


def get_valid_paths_dfs(
    nodes_list: list[Node], start_name: str, end_name: str
) -> list[DevicePath]:
    nodes_map = {node.self_name: node for node in nodes_list}

    start_node = nodes_map.get(start_name)
    if not start_node:
        return []

    queue: list[DevicePath] = [DevicePath(start_node)]

    valid_paths: list[DevicePath] = []
    tested = []

    while queue:

        # print(len(queue))
        current_path = queue.pop(0)
        if current_path in tested:
            continue
        tested.append(current_path)

        current_node = current_path.tail

        for child_name in current_node.children_names:

            # SUCCESS CONDITION
            if child_name == end_name:
                valid_paths.append(current_path)
                continue

            child_node = nodes_map.get(child_name)

            if child_node:
                # loop prevention
                for item in current_path.path:
                    if child_node.self_name == item.self_name:
                        continue

                new_path = copy(current_path)

                new_path.path = current_path.path[:]

                new_path.add_node(child_node)
                queue.append(new_path)

    return valid_paths


def parse_item(text_item: str):
    self_name, children_names = text_item.split(":")
    # print(f"self_name: {self_name}")
    children_names = children_names.strip().split(" ")

    # print(f"children_names: {children_names}")
    return Node(self_name, children_names)


def parse_input(text_in):
    output: list[Node] = []
    for item in text_in:
        item_node = parse_item(item)
        output.append(item_node)
        # print(item_node)
    return output


def solve_part1(text_in):
    nodes_list = parse_input(text_in)
    # print(nodes_list)
    valid_paths = get_valid_paths_dfs(nodes_list, "you", "out")
    return len(valid_paths)


def solve_part2(text_in):
    nodes_list = parse_input(text_in)
    print(f"getting dac2fft")
    dac2fft = get_valid_paths_dfs(nodes_list, "dac", "fft")
    print(f"len(dac2fft): {len(dac2fft)}")
    print()

    print(f"getting dac2out")
    dac2out = get_valid_paths_dfs(nodes_list, "dac", "out")
    print(f"len(dac2out): {len(dac2out)}")
    print()

    print(f"getting svr2dac")
    svr2dac = get_valid_paths_dfs(nodes_list, "svr", "dac")
    print(f"len(svr2dac): {len(svr2dac)}")
    print()

    print("getting svr2fft")
    svr2fft = get_valid_paths_dfs(nodes_list, "svr", "fft")
    print(f"len(svr2fft): {len(svr2fft)}")
    print()

    print("getting fft2dac")
    fft2dac = get_valid_paths_dfs(nodes_list, "fft", "dac")
    print(f"len(fft2dac): {len(fft2dac)}")
    print()

    print("getting fft2out")
    fft2out = get_valid_paths_dfs(nodes_list, "fft", "out")
    print(f"len(fft2out): {len(fft2out)}")
    print()

    output = len(svr2fft) * len(fft2dac) * len(dac2out)

    return output


@aoc_script
def main(file: str = ""):
    text_in = input_to_list(file)
    # print(text_in)
    part1 = solve_part1(text_in)
    print(f"part1: {part1}")
    part2 = solve_part2(text_in)
    print(f"part2: {part2}")


if __name__ == "__main__":
    main()
