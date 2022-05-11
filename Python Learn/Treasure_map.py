row1 = ["[ ]", "[ ]", "[ ]"]
row2 = ["[ ]", "[ ]", "[ ]"]
row3 = ["[ ]", "[ ]", "[ ]"]
map = [row1, row2, row3]
print(f'''
     1      2      3
1 {row1}\n
2 {row2}\n
3 {row3}
''')
position = input("Where do you want to put your treasure?\n")
choice1 = int(position[0])
choice2 = int(position[1])

# if choice1 == 1:
#     index = choice2 - 1
#     row1[index] = "X"
# elif choice1 == 2:
#     index = choice2 - 1
#     row2[index] = "X"
# elif choice1 == 3:
#     index = choice2 - 1
#     row3[index] = "X"

map[choice1 - 1][choice2 - 1] = "X"


print(f'''
     1      2      3
1 {row1}\n
2 {row2}\n
3 {row3}
''')