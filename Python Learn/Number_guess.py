from NG_art import logo
from random import randrange

done = False
while not done:
    print(logo)
    print("Welcome to the Number guessing game.", "I am looking for a number... not smaller than 1 or greater than 100.")

    # This randomly choses an integer from the range of 1 - 100.
    chosen_number = randrange(1, 100, 1)

    attempts = 0
    replies = ["Too Low", "the Correct Answer", "Too High"]
    game_over = False
    difficulty = input("Choose the Difficulty of the game. (easy or hard): ").lower()
    if difficulty == "easy":
        attempts = 10
    elif difficulty == "hard":
        attempts = 5


    def position(number, choice):
        """This checks the relative position of the number guessed to the computer's choice."""
        if number > choice:
            return 2
        elif number < choice:
            return 0
        elif number == choice:
            return 1


    while not game_over:
        print(f"You have {attempts} number of attempts.")
        guess = int(input("What number am I thinking of ? \n"))

        relative_position = position(number=guess, choice=chosen_number)
        answer = replies[relative_position]
        print(f"Your choice is {answer}")
        attempts -= 1

        if relative_position != 1:
            if attempts == 0:
                print("You have run out of chances.")
                print(f"The Correct answer is {chosen_number}")
                game_over = True
            else:
                print("Guess again.")
        else:
            game_over = True

    again = input("Do you want to go again? (Type 'y' or 'n')\n")
    if again == "n":
        done = True

