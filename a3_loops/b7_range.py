# Range doesn't create a new list, it's similar but the magic is in the time building because if we created
example = range(1, 6)
# in this moment we don't have the data 0-10 because it'll created just when we need it.
# Start in zero and don't include the top/up limit but yes the start value.
print(" Example ")
for r in example:
    print(r)

print(" Jumping ")
# obviously we have jumps
for x in range(0, 10, 2):
    print(x)

print(" Range to List ")
number_list = list(range(0, 9))
print("List: ", number_list)

print(
    " Sometimes you need to do just for an exactly number of times, and we have the basic form: "
)
counter_while = 0
while counter_while < 5:
    print(f"{counter_while}: times")
    counter_while += 1

print(" But using the convention _ you can do it more easy: ")
for _ in range(5):
    print(f"{_}: times")
