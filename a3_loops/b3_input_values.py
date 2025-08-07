# In Java we can used the Scanner object but here is more easy.
import os
os.system("cls")

number = -1
while number < 0:
    try:
        number = int(input("Please enter a positive number: "))
        if number < 0:
            pass
    except:
        print("We need a digital no a letter or str!")

print(f"The number the user registered was {number}")