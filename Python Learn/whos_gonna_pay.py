import random

names_string = input("Gimme everybodies name, seperated by a comma \n")
names = names_string.split(", ")
# rand = random.randint(0, (len(names) - 1))
# person = names[rand]
# OR
person = random.choice(names)

print(f"{person} is going to buy the meal today!")
