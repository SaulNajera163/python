# If you know the value that you're waiting but it's just a comment not forced or revise just annotation but we can modified if we want to make a check in the visual studio code.
"""
In easy words, that just annotation but the interpret don't stop her running, just the editor is gonna remember you "Ey bro, be careful because before you said, this variable it's just str and now you are changing to a int.
"""

# preference --> setting --> typecheck --> strict

id_user: bool = True
print(f"Original value: {id_user}")

id_user = False # "Ey bro, you say that values it gonna be just boolean"
print(f"We change the value but at same type {id_user}")

id_user: int = 12334
print(f"We change but another type: {id_user}")

