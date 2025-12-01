import os
import sys

SOLUTION_TEMPLATE = """import sys
from pathlib import Path

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from utils import aoc_script


def input_to_list(file):
    output = []
    file = file.split("\\n")
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
"""


def create_day_files(day_number):
    # Ensure the day_number is valid
    if not (1 <= day_number <= 25):
        print("Error: The day number must be between 1 and 25, inclusive.")
        return

    # Format day number with leading zero (01, 02, etc.)
    day_formatted = f"{day_number:02d}"

    # Define the base path
    base_path = os.path.join(os.getcwd(), "problems", f"day{day_formatted}")

    # Files to be created
    files = {
        "solution.py": SOLUTION_TEMPLATE,
        "input_test.txt": "",
        "input_main.txt": "",
        "__init__.py": "",
    }

    try:
        # Create the day folder
        os.makedirs(base_path, exist_ok=True)
        print(f"Created directory: {base_path}")

        # Create the files in the folder
        for file_name, content in files.items():
            file_path = os.path.join(base_path, file_name)
            with open(file_path, "w") as f:
                f.write(content)
            print(f"Created file: {file_path}")

        print(f"\nDay {day_formatted} setup complete!")
        print(f"Run with: python -m problems.day{day_formatted}.solution [main|test]")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python setup_day.py <day_number>")
        print("Example: python setup_day.py 1")
    else:
        try:
            day_number = int(sys.argv[1])
            create_day_files(day_number)
        except ValueError:
            print("Error: The day number must be an integer.")
