####
# exercises.py
# Ejercicios para practicar los conceptos aprendidos en las lecciones.
###

from os import system

if system("clear") != 0:
    system("cls")

print("\nEjercicio 1: Imprimir mensajes")
print("Escribe un programa que imprima tu nombre y tu ciudad en líneas separadas.")

# name, city = input("Please insert your name and country: \n").split()
# print("----------------------------------------------------------")
# print(name + "\n")
# print(city + "\n")

### Completa aquí
print("--------------")

print("\nEjercicio 2: Muestra los tipos de datos de las siguientes variables:")
print("Usa el comando 'type()' para determinar el tipo de datos de cada variable.")
a = 15
print(type(a))
b = 3.14159
print(type(b))
c = "Hola mundo"
print(type(c))
d = True
print(type(d))
e = None
print(type(e))


### Completa aquí

print("--------------")

print("\nEjercicio 3: Casting de tipos")
print('Convierte la cadena "12345" a un entero y luego a un float.')
print("Convierte el float 3.99 a un entero. ¿Qué ocurre?")

### Completa aquí

print(type(int("1234")))
print(type(float(int("1234"))))
print(f"Round 3.99 {round(3.99)}")

print("--------------")

print("\nEjercicio 4: Variables")
print("Crea variables para tu nombre, edad y altura.")
print("Usa f-strings para imprimir una presentación.")

# "Hola! Me llamo midudev y tengo 39 años, mido 1.70 metros"
my_name = "Saul"
my_age = 24 
my_height = 1.75

print(f"Hi I'm {my_name} and I'm {my_age} years old, finally I'm size {my_height} cm")


### Completa aquí

print("--------------")

print("\nEjercicio 5: Números")
print("1. Crea una variable con el número PI (sin asignar una variable)")
print("2. Redondea el número con round()")
print("3. Haz la división entera entre el número que te salió y el número 2")
print("4. El resultado debería ser 1")

PI = 3.1416 
rounded = round(PI)
divide_by = int(rounded / 2)
print(divide_by)