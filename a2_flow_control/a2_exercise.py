import os
os.system("cls")
# print("----------------First----------------")

# a = int(input("Enter A: "))
# b = int(input("Enter B: "))

# if a > b:
#     print(f"{a} it's largest than {b}")
# else:
#     print(f"{b} it's largest than {a}")

print("----------------Second----------------")

# print("Welcome to our Calculation")
# a = int(input("Enter A: "))
# b = int(input("Enter B: "))

# option = int(input("\n1.-Plus \n2.-Minus \n3.-Divide by \n4.-Product \n5.-Exit" + "\n"))

# if option == 1:
#     print(f"Plus: {a} + {b} is equals -> {a + b}")

# elif option == 2:
#     print(f"Minus: {a} - {b} is equals -> {a - b}")

# elif option == 3:
#     if b == 0:
#         print("We can't divide by Zero!!!!")
#     else:
#         print(f"Divide: {a} by {b} is equals -> {a / b}")

# elif option == 4:
#     print(f"Product: {a} * {b} is equals -> {a * b}")
# else:
#     print("Good bye")


print("----------------Three----------------")


# year = int(input("Enter the year: "))
# if(year % 4 == 0) and ((year % 100 != 0) or (year % 400 == 0)):
#     print(f"Year {year} is busiest ")
# else:
#     print("It's nos busiest")

print("----------------Four----------------")

age = int(input("Enter your age: "))
if age >= 0 and age <= 2:
    print("Baby")
elif age >= 3 and age <= 12:
    print("Boy/Girl")
elif age >= 13 and age <= 17:
    print("Teenager")
elif age >= 18 and age <= 64:
    print("Sr. or Sra.")
else:
    print("Old Sr. or Sra.")
