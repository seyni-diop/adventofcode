"""
Advent of Code 2023 : Day 4
===========================
Seyni DIOP : https://github.com/seyni-diop/adventofcode
"""

def get_my_winning_nums(line: str) -> [int, list]:
    """ To get the winning the card number and all winning number in a line.

    Args:
        line (str): string input (one line)

    Returns:
        [int, list]: first element is the n° of the card and the second is
                     list of winning numbers
    """
    num_card, game = line.split(':')

    winning_nums, my_nums = game.strip().split("|")
    winning_nums = winning_nums.strip().split()
    my_nums=my_nums.strip().split()
    my_winning_nums = [number for number in winning_nums if number in my_nums]
    return int(num_card[5:]), my_winning_nums


def solver_part_1(filepath: str) -> int:
    """Part 1 solver

    Args:
        filepath (str): path of text file

    Returns:
        int: result
    """
    res = 0
    with open(filepath, mode="r", encoding="utf-8") as f:
        while True:
            line = f.readline().strip('\n')
            if not line:
                break
            _ , my_winning_nums = get_my_winning_nums(line)
            if len(my_winning_nums)>0:
                res = res + 2**(len(my_winning_nums)-1)
    return res



def solver_part_2(filepath: str) -> int:
    """Part 2 solver

    Args:
        filepath (str): path of text file

    Returns:
        int: result
    """
    res = 0
    card_copies = {}
    with open(filepath, mode="r", encoding="utf-8") as f:
        while True:
            line = f.readline().strip('\n')
            if not line:
                break
            num_card, my_winning_nums = get_my_winning_nums(line)
            for i in range(1, len(my_winning_nums)+1):
                card_copies.update(
                    {num_card+i: card_copies.get(num_card, 0) + card_copies.get(num_card+i, 0) + 1})
            res += 1
    res += sum(card_copies.values())
    return res

assert solver_part_1('test.txt') == 13, "Solution part 1 fails."
assert solver_part_2('test.txt') == 30, "Solution part 2 fails."

if __name__ == "__main__":
    print(f"Solution part 1: {solver_part_1('input.txt')}")
    print(f"Solution part 2: {solver_part_2('input.txt')}")
