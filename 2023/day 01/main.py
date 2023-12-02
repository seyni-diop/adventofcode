"""
Advent Code 2023 : Day 1
========================
Seyni DIOP : https://github.com/seyni-diop/adventofcode

"""

import re
from copy import copy
from typing import Callable

def get_calibration_1(line: str):
    """Part 1 function

    Args:
        line (str): _description_

    Returns:
        _type_: _description_
    """
    y = re.findall(r'\d', line)
    return int(y[0]+y[-1])

def get_calibration_2(line: str) -> int:
    """Part 2 function

    Args:
        line (str): string input 

    Returns:
        int: _description_
    """
    # letter by digit dict match
    letter_to_digit = {'one':'1','two':'2', 'three':'3',
                       'four':'4', 'five':'5','six':'6',
                       'seven':'7', 'eight':'8', 'nine':'9'}

    # substitute pattern
    line_sub = copy(line)
    for let, dig in letter_to_digit.items():
        l_pos = line_sub.find(let)
        if l_pos != -1:
            line_sub = line_sub[:l_pos+1] + dig + line_sub[l_pos+1:]

        r_pos = line_sub.rfind(let)
        if r_pos != -1:
            line_sub = line_sub[:r_pos+1] + dig + line_sub[r_pos+1:]

    # use get_calibration_1 to get right calibration value
    res = get_calibration_1(line_sub)
    return res

def solver(filepath: str, calibration_func: Callable) -> int:
    """Return some of all calibration line 

    Args:
        filepath (str): path of text file
        calibration_func (Callable): function to use for calibration compute

    Returns:
        int: sum of all of the calibration values
    """
    res = 0
    with open(filepath, mode="r", encoding="utf-8") as f:
        while True:
            line = f.readline()
            if not line:
                break
            res += calibration_func(line)
    return res

# Test
assert solver("test_1.txt", get_calibration_1)==142, 'Calibration 1 failed'
assert solver('test_2.txt', get_calibration_2)==281, "Calibration 2 failed"
if __name__ == "__main__":
    print(f"Solution part 1: {solver('input.txt', get_calibration_1)}")
    print(f"Solution part 2: {solver('input.txt', get_calibration_2)}")
