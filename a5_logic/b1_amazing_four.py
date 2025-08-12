import os
os.system("cls")

def is_equilibrate(string: str) -> bool:
    count_r = 0
    count_j = 0

    for letter in string:
        if letter == "r" or letter == "R":
            count_r += 1
        elif letter == "j" or letter == "J":
            count_j += 1
    if count_r == count_j:
        return True
    elif count_r != count_j:
        return False
    elif count_r == 0 and count_j == 0:
        return True

