# You just need the name = value and it´s so important to remember, you can re-asignated

my_name = "Saul Najera"
my_age = 24
married = False

# Here we can see some different things against Java because we can not use in the same print a different values without before casting o format them.
print("Who:" + my_name + " " + str(my_age) + " married? " + str(married))
print("---------------------------------------------")

# "f" This is one of the most common form to achieve it because we just use the same sentence as if the values be the same.
print(f"Name: {my_name}  Age:  {my_age} +  Married?  {married}")
print("---------------------------------------------")

# And it's dynamic because we can change variable value.
my_name = 999
print(f"Name: {my_name}  Age:  {my_age} +  Married?  {married}")

# Strong Typing
# print("10" + 3) # ----> Ey bro I'm gonna not change nothing if you don't do it.
# print("---------------------------------------------")
print("---------------------------------------------")

# Formatting with f ----> f-string
degree = "engineer"
years = 4.5
print(
    f"If you want to get a {degree} degree so you need at least {years} years plus 1 year more for the service, finally {years + 1} years"
)

print("---------------------------------------------")
# Here we don't use the camel case, here is snake case
my_variable_is_snake_case = "Here we don't use the camel case, here is snake case"
print(my_variable_is_snake_case)
print("---------------------------------------------")

# Python don't have constant nature but you can use some "tricks" to emulate and use the upper case
MY_CONSTANT = "Python don't have nature constant but you can use some tricks to emulate and use the upper case"
print(MY_CONSTANT)
print("---------------------------------------------")
