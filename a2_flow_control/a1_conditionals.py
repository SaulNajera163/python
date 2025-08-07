# As the same functions in Java
import os  # This is a library like import.java....

os.system("cls")


print("----------------------Basic Condition----------------------")
age = 18
if age >= 18:
    print("You can buy some beer!")
else:
    print("You can not buy a beer!")

print("\n----------------------Multiple If and elif----------------------")

money = 10000
# money = int(input("Enter your salary: "))
if money >= 100000:
    print("You're in Royal socialite")
elif money >= 50000 and money < 100000:
    print("You're in intermediate socialite")
elif money >= 20000 and money < 50000:
    print("Your're average socialite")
else:
    print("You're poor socialite!")

print("\n----------------------Multiple Conditions----------------------")

id_user = 9
available = False

if (id_user <= 10 and id_user > 5) and available:
    print("This was one of our 10 firsts customer!!!")
elif (id_user > 0 and id_user <= 5) and available:
    print("This was one of our 5 firsts customer!!!")
else:
    print("This is nota customer!!!")

print("\n---------------------- Conditions && and ----------------------")

weekend = False
holiday = True
week = True

if holiday and weekend:
    print("We haven't go to the work!")
else:
    print("We have to go working")

print("\n---------------------- Condition || or ----------------------")

# if not holiday or weekend:
#     print("We haven't go to the work!")
# else:
#     print("We have to go working")

print("\n---------------------- If nesting  ----------------------")

# my_age = int(input("Enter your age: "))
# support = None
# if my_age >= 21:
#     my_money = float(input("Enter the average money that you have: "))
#     if my_money <= 50000:
#         support = True
#     else:
#         support = False
# else:
#     print("You need to be 21 years old or more.")

# if support:
#     print("You ticket it's 50 percent discount")
# else:
#     print("You don't need discount")

print("\n ----------------------Ternary Operator----------------------")

a = 100
message = "It's largest " if a > 100 else "It's smaller"
print(f"Message: {message}")