import os

os.system("cls")


def is_equilibrate(txt: str) -> bool:
    """This function just receive a txt and just count R and J because change to upper so if that counts are equals so true"""
    count_r = 0
    count_j = 0
    for letter in txt:
        if letter.upper() == "R":
            count_r += 1
        elif letter.upper() == "J":
            count_j += 1
    print(f"Count of R: {count_r} and Count of J: {count_j}")
    return count_r == count_j

print(is_equilibrate("ldjlawjdjrkrlakkle"))
