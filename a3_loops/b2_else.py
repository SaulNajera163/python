# It's the first time I saw an else in a loops but that it just to indicate or do something when the loop finished.
import os
os.system("cls")

"""
Maybe you think, why used the else and just put the line out site the while, well if you used a break and the loop never finished, so the code never happen
"""

print(" ---------- Here the while always was true and the else never executed ---------- ")
counter = 0 
while counter < 10:
    print(counter)
    counter +=1
    if counter == 5:
        break
else:
    print("This else never happen because the while never finished at 100%")

print(" ---------- Here the while finished and we know we executed all ---------- ")
counter = 0 
while counter < 10:
    print(counter)
    counter +=1
    if counter == 5:
        break
print("This happen at 100%")


