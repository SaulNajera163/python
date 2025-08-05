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

print("Welcome to our Calculation")
a = int(input("Enter A: "))
b = int(input("Enter B: "))

option = int(input("\n1.-Plus \n2.-Minus \n3.-Divide by \n4.-Product \n5.-Exit" + "\n"))

if option == 1:
    print(f"Plus: {a} + {b} is equals -> {a + b}")

elif option == 2:
    print(f"Minus: {a} - {b} is equals -> {a - b}")

elif option == 3:
    if b == 0:
        print("We can't divide by Zero!!!!")
    else:
        print(f"Divide: {a} by {b} is equals -> {a / b}")

elif option == 4:
    print(f"Product: {a} * {b} is equals -> {a * b}")
else:
    print("Good bye")


print("----------------Three----------------")

# Ejercicio 3: Año bisiesto
# Pide al usuario que introduzca un año y determina si es bisiesto.
# Un año es bisiesto si es divisible por 4, excepto si es divisible por 100 pero no por 400.

year = int(input("Enter the year: "))
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    #(anio % 4 == 0) and ((anio % 100 != 0) or (anio % 400 == 0))
    print(f"Year {year} is busiest ")

# Ejercicio 4: Categorizar edades
# Pide al usuario que introduzca una edad y la clasifique en:
# - Bebé (0-2 años)
# - Niño (3-12 años)
# - Adolescente (13-17 años)
# - Adulto (18-64 años)
# - Adulto mayor (65 años o más)
