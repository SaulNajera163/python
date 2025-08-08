import os

os.system("cls")
# Exercise 1: Printing Even Numbers
# Print all even numbers from 2 to 20 (inclusive) using a for loop.
print("\nExercise 1:")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

for n in numbers:
    if n % 2 == 0:
        print(n)

# Exercise 2: Calculating the Mean of a List
# Given the following list of numbers:
# numbers = [10, 20, 30, 40, 50]
# Calculate the mean of the numbers using a for loop.
print("\nExercise 2:")
counter = len(numbers)

total_plus = 0
for n in numbers:
    total_plus += n

print("Mean: ", total_plus / counter)

# Exercise 3: Finding the Maximum in a List
# Given the following list of numbers:
# numbers = [15, 5, 25, 10, 20]
# Find the maximum in the list using a for loop.
print("Exercise 3:")
numbers_three = [15, 5, 25, 29, 20]
start = numbers_three[0]
for n in numbers_three:
    if start < n:
        start = n
print(start)

# Exercise 4: Filtering Strings by Length
# Given the following list of words:
# words = ["house", "tree", "sun", "elephant", "moon"]
# Create a new list containing only words with more than 5 letters
# using a for loop and list comprehension.
print("Exercise 4:")
words = ["house", "tree", "sun", "elephant", "burgers"]
new_list = [w for w in words if len(w) <= 5]
print("Minus: ", new_list)


# Exercise 5: Counting Words That Begin with a Letter
# Given the following list of words:
# words = ["house", "tree", "sun", "elephant", "moon", "car"]
# Ask the user to enter a letter.
# Count how many words in the list begin with that letter (case-insensitive).
print("Exercise 5:")
letter = input("Enter the letter: ")
words_five = ["house", "tree", "sun", "elephant", "burgers", "Tango"]

counter = 0
for w in words_five:
    if w.lower().startswith(letter):
        counter += 1
print(f"In the list, there are {counter} words_five that starts with {letter}")
