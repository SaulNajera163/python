# As in java with the Scanner scanner =  System.in ---> here is input()

name = input("Enter your name:\n")
print(f"Hi and welcome Sr: {name}, would you like a beer?")

# input always receive a srt so, you can not plus a str and int but you can use the wrapper form

age = int(input("How old are you Sr. {name}?"))
print(f"In 30 years you're be {age + 30} years") 

#Here is so crazy 'cause in java I can't do that, but we can multiple data at the same time but the key is using split() is based in the spaces.
print("Enter your address and your country: ")
address, country = input("Address and Country:\n").split()

print(f"Your country is: {country} and your address is: {address} .")