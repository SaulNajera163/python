import os
os.system("cls")

print(" -------------- While --------------")
# counter = 0
# while counter <= 5:
#     print(counter)
#     counter += 1


print(" -------------- Breaking -------------- ")
# counter = 0
# while counter <= 100:
#     print(counter)
#     counter += 1
#     if counter % 9 == 0:
#         break

print(" -------------- Continue -------------- ")
number = 0
while number <= 20:
    number += 1
    if number % 2 == 0:
        continue
    # The next code it's never running, directly drive to the while.
    print(number)