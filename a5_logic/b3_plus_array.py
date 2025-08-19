import os

os.system("cls")

"""We need to get a list of numbers and this is as five or six position but the important thing here is, we'll give it a number and we tried to find the firsts two position
than plus them, give us the number result"""

numbers = [2, 9, 3, 1, 1, 4, 2]
goal = 5


def list_and_goal(list_numbers: list[int], goal: int) -> None | list[int]:
    for i in range(len(list_numbers) - 1):
        for j in range(i + 1, len(list_numbers)):
            if i + j == goal:
                return [i,j]


print()
