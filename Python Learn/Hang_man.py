import random

stages = ['''
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["ardvark", "baboon", "camel"]
lives = 6
end_of_game = False


chosen_word = random.choice(word_list)

display = []
word_lenght = len(chosen_word)

for index in range(word_lenght):
    display.append("_")

while not end_of_game:
    guess = input("Guess a letter in the word\n").lower()

    for position in range(word_lenght):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = guess
    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            print("You lose")
            end_of_game = True
   
    if "_" not in display:
        print("You win")
        end_of_game = True

    # Print display
    print(f"{' '.join(display)}")
    
    print(stages[lives])