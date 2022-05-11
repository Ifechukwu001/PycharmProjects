import math

def paint_calc(height, width, cover):
    can_number = math.ceil((height * width) / cover) # The ceil function in math is for rounding up the number cinstantly
    print(f"You'll need {can_number} cans of paint.")


test_h = int(input("Height of wall: "))
test_w = int(input("width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
