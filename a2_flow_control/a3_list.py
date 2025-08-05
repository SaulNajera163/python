# Here the lists are so crazy because we have many different easy form to use them.
import os

os.system("cls")


list_int = [1, 2, 3, 4, 5]
list_float = [2.3, 0.4, 25.5, 0.4, 99.9]
list_str = ["Start", "Veronica", "Intermediate", "Gilberto", "End"]

# if we have the type checking in the setting, we can have list of several different types.
# list_min: list[int | str | float | bool] = [1, "String", 3.24, True]

list_empty = []
list_of_list = [[1, 2], [3, 4]]
matrix = [[10, 20], [30, 40], [50, 60]]

print("------------------- My basic lists -------------------")
print(list_int)
print(list_float)
print(list_str)
print(list_empty)
print(list_of_list)
print(matrix)

# And we can use the negative index.
print("------------------- Access lists -------------------")
print(list_int[0])
print(list_float[4])
print("Here is crazy but I can use negative index positions")
print(list_str[-1])
print(list_str[-5])

print("------------------- Matrix -------------------")
matrix = [[10, 20], [30, 40], [50, 60]]
print(matrix[0][1])

# Here is not usually use substring instead of we use just the index and  start:end:pass
print("------------------- Slicing [ start : end : pass ]-------------------")
list_int = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print("\nIf I want 2-8 we can use [1:8] but the limits are not taking")
print(list_int[1:8])

print("\nThe 5 firs ---> [:5] ---> [start:5] from start to 5")
print(list_int[:5])

print("\nThe 5 lasted ----> [5:] ---> [5:end] from 5 to end")
print(list_int[5:])

print("\nWe can create a copy using [:] ---> this indicate from start to end")
list_int_copy = list_int[:]
print(list_int_copy)

print("----------------------- Pass ------------------------")
print(list_int_copy)
print("\nWhen we use the three parameter, we're saying how we want move on the list")
print(
    "\nStart = 1 and not is taking so take the second, -1 is the last position and don't taking but 2 is the jumps."
)
print(list_int_copy[1::2])

print(
    "\nStart = 0, so take the first, end at the end and it's taking the end and the jump is 2."
)
print(list_int_copy[::2])

print(
    "\nThis is so crazy 'cause in Java to change a complete list in reverse, we need the loops and some logic, here not"
)
list_int_copy_reverse = list_int_copy[::-1]
print(list_int_copy)
print(list_int_copy_reverse)
