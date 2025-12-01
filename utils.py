import os
import sys
from pathlib import Path


def clear_terminal():
    print("\033[H\033[J")


def read_file(filename):
    with open(filename, "r") as f:
        return f.read()


def get_usage_type():
    try:
        argument = sys.argv[1]
        if argument not in ["main", "test"]:
            print("Argument can be either main or test.")
            exit(0)
        else:
            return argument
    except IndexError:
        return "test"


def aoc_script(func):
    def wrapper():
        # Boilerplate code to run before main function
        clear_terminal()

        # Get the directory of the script that's using this decorator
        import inspect

        caller_frame = inspect.stack()[1]
        caller_file = caller_frame.filename
        script_dir = Path(caller_file).parent

        file = ""
        usage_type = get_usage_type()

        if usage_type == "main":
            file_path = script_dir / "input_main.txt"
        elif usage_type == "test":
            file_path = script_dir / "input_test.txt"

        file = read_file(file_path)

        # Call the original function with the file
        return func(file)

    return wrapper
