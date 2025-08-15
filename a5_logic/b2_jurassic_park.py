import os

os.system("cls")

start_list = [21, 54, 2, 44, 46, 75, 775, 534, 23, 345, 23, 21, 24, 56, 13, 60]


def jurassic_eggs(eggs_list: list[int]) -> tuple[list[int], int]:
    """Returns a list of even integers from the input list"""
    counter = 0
    par: list[int] = []
    for egg in eggs_list:
        if egg % 2 == 0:
            par.append(egg)
            counter += egg
    return par, counter


result_list, total = jurassic_eggs(start_list)
print(f"Complete list: {result_list} and the total par plus is: {total} ")
