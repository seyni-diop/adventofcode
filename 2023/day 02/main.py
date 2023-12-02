"""
Advent Code 2023 : Day 02
=========================
Seyni DIOP : https://github.com/seyni-diop/adventofcode

"""
import numpy as np

def get_max_denom(game_sets: str) -> dict:
    """Get the "max" possible game

    Args:
        game_sets (str):

    Returns:
        dict: Possible game
    """
    max_denom = {'red':0, 'green': 0, 'blue':0}

    for one_set in game_sets.split(';'):
        set_splitted = one_set.split(',')
        for i in set_splitted:
            a = i.strip().replace('  ',' ').split(' ')
            if max_denom[a[1]]<int(a[0]):
                max_denom.update({a[1]: int(a[0])})

    return max_denom

def get_pos_number(line: str, valid_bag: dict) -> int:
    """Function that return the game number if it's possible else return 0

    Args:
        line (str): path of text file
        valid_bag (dict): 

    Returns:
        _type_: result
    """
    x = line.split(':')
    game_num, game_sets = x[0][5:], x[1]
    max_denom = get_max_denom(game_sets)
    res = all(valid_bag[k] >= v for k, v in max_denom.items())

    return int(game_num) if res else 0


def solver_part_1(filepath: str, valid_bag: dict) -> int:
    """Solver of part 1

    Args:
        filepath (str): path of text file
        valid_bag (dict): accepted bag of cubes

    Returns:
        int:  result
    """
    result = 0
    with open(filepath, mode="r", encoding="utf-8") as f:
        while True:
            line = f.readline()
            if not line:
                break
            result += get_pos_number(line, valid_bag)
    return result

def solver_part_2(filepath: str) -> int:
    """Solver of part 1

    Args:
        filepath (str):  path of text file

    Returns:
        int: result
    """
    result = 0
    with open(filepath, mode="r", encoding="utf-8") as f:
        while True:
            line = f.readline()
            if not line:
                break
            x = line.split(':')
            max_denom = get_max_denom(x[1])

            result += np.prod(list(max_denom.values()))
    return result

assert solver_part_1('test.txt', {"red": 12, "green": 13, "blue": 14}) == 8,\
    "Solution part 1 failed. Correct the code"

assert solver_part_2('test.txt') == 2286,"Solution part 2failed. Correct the code"

if __name__ == "__main__":
    accepted_bag = {"red": 12, "green": 13, "blue": 14}
    print(f"Solution part 1: {solver_part_1('input.txt', accepted_bag)}")
    print(f"Solution part 2: {solver_part_2('input.txt')}")
