# Creatin a love calculator.

print("Welcome to the Love Calculator.")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

name11 = name1.lower()
name22 = name2.lower()

t = name11.count("t") + name22.count("t")
r = name11.count("r") + name22.count("r")
u = name11.count("u") + name22.count("u")
e = name11.count("e") + name22.count("e")
l = name11.count("l") + name22.count("l")
o = name11.count("o") + name22.count("o")
v = name11.count("v") + name22.count("v")
e1 = name11.count("e") + name22.count("e")

dig1 = t + r + u + e
dig2 = l + o + v + e1

result = str(dig1) + str(dig2)

if result < "10" or result > "90":
    print(f"Your score is {result}, you go together like coke and mentos :]")
elif "40" < result < "50":
    print(f"Your score is {result}, you go well together :0")
else:
    print(f"Your score is {result}")