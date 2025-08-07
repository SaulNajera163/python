import os
os.system("cls")

print(" --------------------------- First --------------------------- ")
list_secret = ["C","o","d","i","g","o"," ","s","e","c","r","e","t","o"]
print(list_secret[7:])

print(" --------------------------- Second --------------------------- ")
numbers = [10,20,30,40,50]
numbers[0] = 100 
numbers[-1] = -100
print("List: ", numbers)

print(" --------------------------- Three --------------------------- ")
pan = ["pan arriba"]
ingredientes = ["jamos","queso","tomate"]
pan_abajo = ["pan abajo"]
sandwich = pan[:] , ingredientes[:], pan_abajo[:]
print("Sandwich: ", sandwich)

print(" --------------------------- Four --------------------------- ")
list_original = [1,2,3]
list_copy = list_original[:] + list_original
print(list_copy)

print(" --------------------------- Five --------------------------- ")
lista = [10, 20, 30, 40, 50]
center = len(lista) // 2
print(lista[center])

print(" --------------------------- Six --------------------------- ")
# Ejercicio 6: Reversa parcial
print("\nEjercicio 6:")
original = [1,2,3,4,5,6,7,8,9,10]
center = len(original) // 2
reverse_half = original[:center][::-1] + original[center:]
print(reverse_half)