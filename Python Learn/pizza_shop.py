# Creating a pizza api :)

print("Welcome to Python Pizza Deliveries.")

size = input("What size of pizza do you want? S, M or L: ")
add_peperroni = input("Do you want peperroni? Y or N: ")
extra_cheese = input("Do you want cheese? Y or N: ")

bill = 0

if size == "S":
    bill += 15
elif size == "M":
    bill += 20
else:
    bill += 25

if add_peperroni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is now ${bill}")