# For
import os

os.system("cls")
print(" ----------------- For -----------------")
list = ["A", "B", "C", "D", "E", "F", "G"]

for item in list:
    print(item)

print(" ----------------- Any object iterative -----------------")
string = "This is a string"
for letter in string:
    print(letter)

print(" ----------------- Index and Value -----------------")
for i, value in enumerate(list):  # Always it's first the index and later the value
    print(f"Position {i} is the {value}")

print(" ----------------- Loops inside other loops -----------------")

strings = ["d", "w", "g"]
numbers = [2, 6, 7]

for s in strings:
    for n in numbers:
        print(f"[ {s} , {n} ]")

print(" ----------------- Break and Continue -----------------")

songs = ["AC/DC", "Kiss", "Gloria", "The beatles", "Buki" "Natalia"]

for s in songs:
    if s == "Kiss":
        break
    print("Song: ", s)

print(" --- --- --- --- --- ")

for s in songs:
    if s == "Gloria":
        continue
    print("Song: ", s)

print(" --- --- --- --- --- ")
for i, x in enumerate(songs):
    print(f"{i}.- {x}")

print(
    " --- --- -  List Comprehension - --- --- "
)  # The key Idea it that return a new list.
gmails = ["Saul@gmail.com", "JuaN@gmail.com", "Lopez@gmail.com", "CarloS@gmail.com"]
gmails_parse = [g.lower() for g in gmails]
print(gmails_parse)


print(" --- --- -  List Comprehension showing par - --- --- ")
par = [num for num in [234, 12, 24, 53, 4, 12, 45, 665, 234, 45, 2] if num % 2 == 0]
print("Par: " , par)


