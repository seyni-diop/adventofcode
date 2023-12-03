"""
Advent of Code 2023 : Day 3
===========================
Seyni DIOP : https://gitlab.com/seyni_diop/advent-of-code
"""

import re
import numpy as np

def solver_part_1(filepath: str) -> int:
    """Part 1 solver

    Args:
        filepath (str): path of text file

    Returns:
        int: result
    """
    # Initialize regex
    num_finder = re.compile(r'(\d+)')
    symbol_finder = re.compile(r'[^0-9, ^.]')
    result = 0
    with open(filepath, mode="r", encoding="utf-8") as f:
        # Read all lines (/!\ avoid \n)
        lines = f.read().splitlines()

        for i, line in enumerate(lines):

            # select lines at the top, bottom and the line itself
            sub_lines = lines[max(i-1, 0): i+2]

            # iterate according to the numbers found on the line
            for num in num_finder.finditer(line):
                # build a character string that will tell us if the number has an adjacent symbol.
                x = ''
                pos = num.start()
                num_value = num.group()
                length = len(num_value)
                for sub_line in sub_lines:
                    x = x + sub_line[max(pos-1, 0) : pos+length+1]

                # check if x contains a symbol
                if len(symbol_finder.findall(x)) > 0:
                    result += int(num_value)
    return result


def solver_part_2(filepath: str) -> int:
    """Part 2 solver

    Args:
        filepath (str): path of text file

    Returns:
        int: result
    """
    star_finder = re.compile(r'\*')
    num_finder = re.compile(r'(\d+)')
    result = 0
    with open(filepath, mode="r", encoding="utf-8") as f:
        # Read all lines (/!\ avoid \n)
        lines = f.read().splitlines()

        for i, line in enumerate(lines):
            # select lines at the top, bottom and the line itself
            sub_lines = lines[max(i-1, 0):i+2]

            # iterate according to the start found on the line
            for star in star_finder.finditer(line):

                star_pos = star.start()
                gear_nums = []

                for sub_line in sub_lines:
                    for num in num_finder.finditer(sub_line):
                        # check if the number may be in the gear number list of the *
                        if num.start()-1 <= star_pos <= num.end():
                            gear_nums.append(int(num.group()))
                # check if the * have more than two numbers (for product)
                if len(gear_nums) >= 2:
                    result = result + np.prod(gear_nums)
    return result

assert solver_part_1('test.txt') == 4361, "Test 1 failed"
assert solver_part_2('test.txt') == 467835, "Test 2 failed"

if __name__ == "__main__":
    print(f"Solution part 1: {solver_part_1('input.txt')}")
    print(f"Solution part 2: {solver_part_2('input.txt')}")