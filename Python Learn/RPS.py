import random
rock = '''
    __________
---'   _______)
      (_______)
      (______)
      (_____)
---,__(____)
'''

paper = '''
    _________
---'   ______)___
          _______)_
          _________)
          ________)
---,____________)
'''

scissors = '''
    _________
---'   ______)____
      (___________)
      (_________)
      (_____)
---,__(____)
'''

options = [rock, paper, scissors]
choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors.\n"))
print(f"You choose {choice}", options[choice], sep="\n")
sys_choice = random.randint(0, 2)
print(f"Computer choose {sys_choice}", options[sys_choice], sep="\n")

if choice == 0 and sys_choice == 2:
    print("You win.")
elif choice == 2 and sys_choice == 0:
    print("You lose.")
elif choice > sys_choice:
    print("You win.")
else:
    print("You lose.")