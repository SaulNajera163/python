#
import os

os.system("cls")

print(" ---------------------- Plus ----------------------")


def plus(a: float, b: float) -> float:
    """This is just the form to documentation so in this example, you need two numbers and these must be float, the function take both numbers and created plus between numbers, later return the value but just the value"""
    return a + b


print(plus(3, 2))


# parameter are in the function structure
# argument is the value the is wrote when you called the function
def hello(greeting: str):
    print(greeting)


hello("Hello")

print(" ---------------------- Help function ----------------------")
# help(plus)

print(" ---------------------- Static parameters ----------------------")


def product(a: int, b: int = 2) -> int:
    return a * b


print(product(10))

print(" ---------------------- Position Parameters ---------------------- ")


def greeting(name: str, surname: str, work: str, age: int):
    print(f"Hi Sr. {surname} {name}, you're our {work} and you are {age} years old!")


# greeting("Saul", "Najera", 24, "Engineer") # As you wrote your parameters in your function, you have to follow the same order
greeting(
    "Saul", "Najera", "Engineer", 24
)  # As you wrote your parameters in your function, you have to follow the same order


# def several(*args: int):
#     suma = 0
#     for n in args:
#         suma += n
#     return suma


# print(several(1, 2, 3, 34, 5, 55))
print("\n")


def key_value(**kwargs: str) -> None:
    for key, value in kwargs.items():
        print(f"Key: {key} - Value: {value}")


key_value(name="First ", age="second", year="2024")
print("\n")
key_value(name="First ", age="second", year="2024", account="23")
print("\n")
