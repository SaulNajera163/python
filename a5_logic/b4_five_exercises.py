# You can move the different parameters as you need it.
import os

os.system("cls")


def greeting(name: str, age: int, sentence: str):
    print(f"Hello {name} you're {age} years old, {sentence}")


greeting("Saul", 24, "Welcome to the world of Python")


def arguments(*args: int) -> int:
    p: int = 0
    for num in args:
        p += num
    return p


print(arguments(1, 2, 2, 212, 1, 21, 2, 12, 2), "\n")


def key_value(**kwargs: int | str | float | bool) -> None:
    for key, value in kwargs.items():
        print(f"{key} = {value}")


key_value(name="saul", age=24, salary=2500.99)
print("\n")
key_value(name="Ivonne", married=False, age=23, salary=999.99)
print("\n")
