"""
Casting of types is so normal
"""

#

print(
    "Conversion of type ---> Don't do the automatic conversion because it's Strong typing"
)

print("--------------------------------------------")

print(type(int("100")))
# Conversion
a = int("100") + 12
print(a)
print("--------------------------------------------")

print(type(float("21.21")))

print(int(2342.23232))  # be careful because that lose data.
print(int(2.6))

print("--------------------------------------------")

# All that are not be 0 it's gonna be True
print(bool(1))
print(bool(-13))
print(bool(0))
print("--------------------------------------------")

# All that are not be "" it's gonna be true

print(bool("dwandhiw"))
print(bool("Saul"))
print(bool(""))
print(bool(" "))

#Be so careful because python round to the next pair not the exactly first number when always is .5 exactly
print("Always round to the next pair more earlier")
print(round(1.5)) #The earlier pair it's 2
print(round(2.5)) #Here is the same
print(round(2.51)) # Normal to the top up.
print(round(3.5))