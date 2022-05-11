# Trying to creat a leap year program using a very complex flowchart.
# Watch carefully.

year = int(input("Enter the year you want to test: "))
output = ""

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            output = "a Leap year"
        else:
            output = "Not a leap year"
    else:
        output = "a Leap year"
else:
    output = "Not a leap year"

print(f"The year {year} is {output}")