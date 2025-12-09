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


@aoc_script
def main(file: str = ""):
    text_in = input_to_list(file)
    print(text_in)


if __name__ == "__main__":
    main()
