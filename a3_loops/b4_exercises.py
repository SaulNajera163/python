import os

os.system("cls")
###
# EJERCICIOS (while)
###

# Ejercicio 1: Cuenta atrás
# Imprime los números del 10 al 1 usando un bucle while.
print("\nEjercicio 1:")
count = 10
while count > 0:
    print("Count: ", count)
    count -= 1


# Ejercicio 2: Suma de números pares (while)
# Calcula la suma de los números pares entre 1 y 20 (inclusive) usando un bucle while.
print("\nEjercicio 2:")
counter = 1
plus = 0
while counter <= 20:
    if counter % 2 == 0:
        plus += counter
    counter += 1
print("Plus: ", plus)

# Ejercicio 3: Factorial de un número
# Pide al usuario que introduzca un número entero positivo.
# Calcula su factorial usando un bucle while.
# El factorial de un número entero positivo es el producto de todos los números del 1 al ese número. Por ejemplo, el factorial de 5
# 5! = 5 x 4 x 3 x 2 x 1 = 120.
print("\nEjercicio 3:")
# fac = int(input("Enter the number to know the factorial: "))

# factorial = 1
# while fac > 0:
#     factorial *= fac
#     fac -= 1
# print(factorial)


# Ejercicio 4: Validación de contraseña
# Pide al usuario que introduzca una contraseña.
# La contraseña debe tener al menos 8 caracteres.
# Usa un bucle while para seguir pidiendo la contraseña hasta que cumpla con los requisitos.
# Si la contraseña es válida, imprime "Contraseña válida".
print("\nEjercicio 4:")
# agree = False
# while agree != True:
#     password = input("Enter you new password:\n")
#     letter = len(password)
#     if letter >= 8:
#         print("Welcome!")
#         agree = True


# Ejercicio 5: Tabla de multiplicar
# Pide al usuario que introduzca un número.
# Imprime la tabla de multiplicar de ese número (del 1 al 10) usando un bucle while.
print("\nEjercicio 5:")
# number = int(input("Enter your number: "))
# counter = 1
# while counter <= 10:
#     print(number * counter)
#     counter += 1

# print("\nEjercicio 6.1:")

# # First we'll created a easy example to know if the number enter is prime
# count = 2
# prime = True
# n = int(input("Enter a number: "))
# if n > 1:
#     while count < n:
#         if n % count == 0:
#             prime = False
#             break
#         count += 1
# elif n == 1 or n < 0:
#     prime = False

# print(f"Number {n} is it prime? ", prime)


# This code is to show the prime numbers of a X number enter by the user.
print("\nEjercicio 6.2:")
n = int(input("Introduce un número entero positivo N: "))
start = 2 # We can't not start from 0 or 1 so we'll take the 2
while start <= n: # The final purpose it's reach the n number 
    prime = True  # Suponemos que es primo inicialmente
    counter = 2
    while counter < start:  # Comprobamos counteres desde 2 hasta start-1
        if start % counter == 0:
            prime = False  # Si es divisible, no es primo
            break
        counter += 1
    if prime:
        print(start)
    
    start += 1