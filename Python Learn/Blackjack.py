import random
from BJ_logo import logo

card_lib = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

user_cards = []
dealer_cards = []
user_cards_no = 0
dealer_cards_no = 0
game_on = True


def deal(cards, u_card, d_card):
    """Deals a single card to the user and the dealer"""
    card = random.choice(cards)
    u_card.append(card)
    card2 = random.choice(cards)
    d_card.append(card2)


def game_test(card_lib, u_card_no, d_card_no, user_card):
    if d_card_no == 21:
        return "You lose."
    elif u_card_no == 21:
        return "You win."
    elif u_card_no > 21:
        if card_lib[0] in user_card:
            for card in user_card:
                if card_lib[0] == card:
                    u_card_no -= 10
            if u_card_no > 21:
                return "You lose."
        else:
            return "You lose."


deal(card_lib, user_cards, dealer_cards)
dealer_card1 = dealer_cards[0]

while game_on:
    print(logo)
    deal(card_lib, user_cards, dealer_cards)
    for card in user_cards:
        user_cards_no += card
    for card in dealer_cards:
        dealer_cards_no += card

    outcome = game_test(card_lib=card_lib, u_card_no=user_cards_no, d_card_no=dealer_cards_no, user_card=user_cards)

    print(f"Your cards: {user_cards}", f"Sum of Your Cards: {user_cards_no}", sep="\t")
    print(f"Dealer's first card: {dealer_card1}")

    if outcome == "You lose." or outcome == "You win.":
        game_on = False
        print(outcome)
        continue

    should_continue = input("\nType 'y' to draw another card or 'n' to finish\n")
    if should_continue == "n":
        while dealer_cards_no < 18:
            deal(card_lib, user_cards, dealer_cards)
            user_cards.pop(-1)
            dealer_cards_no = 0
            for card in dealer_cards:
                dealer_cards_no += card

        print(f"Your cards: {user_cards}", f"Sum of Your Cards: {user_cards_no}", sep="\t")
        print(f"Dealer's cards: {dealer_cards}", f"Sum of Dealer's Cards: {dealer_cards_no}", sep="\t")

        if dealer_cards_no > 21:
            print("You win.")
        elif user_cards_no > dealer_cards_no:
            print("You win.")
        elif user_cards_no == dealer_cards_no:
            print("Draw")
        elif user_cards_no < dealer_cards_no:
            print("You lose.")
        game_on = False
    else:
        user_cards_no = 0
        dealer_cards_no = 0
