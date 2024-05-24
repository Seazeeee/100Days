############### Blackjack Project #####################

# Difficulty Normal 😎: Use all Hints below to complete the project.
# Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
# Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
# Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################


# TODO

# Create a function that ask if they want to play again. | Done but sloppy
# Check is dealer gets aces. | Have to test
# Fix the user score inside of the 'n' portion of the if


# Hint 1: Go to this website and try out the Blackjack game:
#   https://games.washingtonpost.com/games/blackjack/
from art import logo
import random


def get_starter_cards():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    card1 = cards[random.randint(0, len(cards) - 1)]

    card2 = cards[random.randint(0, len(cards) - 1)]

    total = card1 + card2

    return card1, card2, total


def get_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    card1 = cards[random.randint(0, len(cards) - 1)]

    return card1


def aces(user_card1, user_card2):

    if user_card1 == 11 and user_card2 == 11:
        ask_about_aces = input("Would you like to play one or both as '1'?: ")

        if ask_about_aces == "one":
            user_card1 = 1
            print(f"Your cards: are now [{user_card1}, {user_card2}]")
            return user_card1, user_card2, False

        elif ask_about_aces == "both":
            user_card1 = 1
            user_card2 = 1
            print(f"Your cards: are now [{user_card1}, {user_card2}]")
            return user_card1, user_card2, False
    else:
        print(
            "You have an ace. You may go over 21 and this will then be counted as 1. "
        )
        return user_card1, user_card2, True
    
def create_cardList():
    user_card1, user_card2, user_total = get_starter_cards()
    dealer_card = get_card()
    dealer_total = dealer_card

    card_list = [
        {
            "user": [user_card1, user_card2],
        },
        {"computer": [dealer_card]},
    ]

    return card_list, user_total, dealer_total

def blackjack():

    hit_question = True
    recursion_total_user = user_total
    recursion_total_dealer = dealer_total

    while hit_question:
        if input("Type 'y' to get another card, type 'n' to pass: \n") == "y":
            new_card = get_card()
            card_list[0]["user"].append(new_card)
            recursion_total_user = sum(card_list[0]["user"])

            dealer_new_card = get_card()
            card_list[-1]["computer"].append(dealer_new_card)
            recursion_total_dealer = sum(card_list[-1]["computer"])

            if recursion_total_user == 21:
                print(
                    f"Your final hand: {card_list[0]['user']}, final score: {recursion_total_user}"
                )
                print(
                    f"Computer's final hand: {card_list[-1]['computer']}, final score: {recursion_total_dealer}"
                )
                print("YOU HIT 21! NICE, YOU WIN! \n")
                hit_question = False

            elif recursion_total_dealer == 21:
                print(
                    f"Your final hand: {card_list[0]['user']}, final score: {recursion_total_user}"
                )
                print(
                    f"Computer's final hand: {card_list[-1]['computer']}, final score: {recursion_total_dealer}"
                )
                print("Dealer hit 21! You lose. \n")
                hit_question = False

            elif recursion_total_user > 21:
                if ace_check:
                    for num in card_list[0]["user"]:
                        if num == 11:
                            get_index = card_list[0]["user"].index(num)
                            card_list[0]["user"][get_index] = 1
                            recursion_total_user = sum(card_list[0]["user"])
                            ace_check = False
                            print("You went over 21!")
                            print(
                                f"Your new card hand is: {card_list[0]['user']}, current score: {recursion_total_user}"
                            )
                            print(
                                f"Computers hand:  {card_list[-1]['computer']}, current score: {recursion_total_dealer}"
                            )
                else:
                    print(
                        f"Your final hand: {card_list[0]['user']}, final score: {recursion_total_user}"
                    )
                    print(
                        f"Computer's final hand: {card_list[-1]['computer']}, final score: {recursion_total_dealer}"
                    )
                    print("You went over! You lose! \n")

                    hit_question = False

            elif recursion_total_dealer > 21:
                for num in card_list[-1]["computer"]:
                        if num == 11:
                            get_index = card_list[-1]["computer"].index(num)
                            card_list[-1]["computer"][get_index] = 1
                            recursion_total_dealer = sum(card_list[-1]["computer"])
                            print("The computer went over 21!")
                            print(
                                f"Your card hand is: {card_list[0]['user']}, current score: {recursion_total_user}"
                            )
                            print(
                                f"Computers new hand:  {card_list[-1]['computer']}, current score: {recursion_total_dealer}"
                            )

                print(
                    f"Your final hand: {card_list[0]['user']}, final score: {recursion_total_user}"
                )
                print(
                    f"Computer's final hand: {card_list[-1]['computer']}, final score: {recursion_total_dealer}"
                )
                print("The dealer went over! You win! \n")

                hit_question = False

            else:
                print(
                    f"Your cards:  {card_list[0]['user']}, current score: {recursion_total_user}"
                )
                print(
                    f"Computers hand:  {card_list[-1]['computer']}, current score: {recursion_total_dealer}"
                )
                hit_question = False
                blackjack()

        else:

            if sum(card_list[-1]["computer"]) <= 17:
                dealer_new_card = get_card()
                card_list[-1]["computer"].append(dealer_new_card)
                recursion_total_dealer = sum(card_list[-1]["computer"])
                print(
                    f"Computer has drawn a card, their hand is now {card_list[-1]['computer']}"
                )

            if recursion_total_dealer == recursion_total_user:
                print(
                    f"Your final hand: {card_list[0]['user']}, final score: {recursion_total_user}"
                )
                print(
                    f"Computer's final hand: {card_list[-1]['computer']}, final score: {recursion_total_dealer}"
                )
                print(f"It's a Draw!")
                hit_question = False
            elif recursion_total_dealer > 21:
                print(
                    f"Your final hand: {card_list[0]['user']}, final score: {recursion_total_user}"
                )
                print(
                    f"Computer's final hand: {card_list[-1]['computer']}, final score: {recursion_total_dealer}"
                )
                print("The dealer went over! You win! \n")

                hit_question = False
            elif recursion_total_dealer > recursion_total_user:
                print(
                    f"Your final hand: {card_list[0]['user']}, final score: {recursion_total_user}"
                )
                print(
                    f"Computer's final hand: {card_list[-1]['computer']}, final score: {recursion_total_dealer}"
                )
                print(f"You lose.")
                hit_question = False

            else:
                print(
                    f"Your final hand: {card_list[0]['user']}, final score: {recursion_total_user}"
                )
                print(
                    f"Computer's final hand: {card_list[-1]['computer']}, final score: {recursion_total_dealer}"
                )
                print(f"You win!")
                hit_question = False


print(logo)

continue_flag = True

while continue_flag:
    card_list, user_total, dealer_total = create_cardList()

    print(f"Your cards: {card_list[0]['user']}, current score: {user_total}")

    print(f"Computer's first card: {str(card_list[-1]['computer'])[1:-1]}")

    if user_total == 21:
        print("YOU WIN!")
    elif 11 in card_list[0]["user"][:]:
        user_card1, user_card2, ace_check = aces(card_list[0]['user'][0], card_list[0]['user'][-1])
        card_list[0]["user"].clear()
        card_list[0]["user"].append(user_card1)
        card_list[0]["user"].append(user_card2)
        blackjack()
    else:
        ace_check = False
        blackjack()

    while continue_flag:
        if input("Would you like to play again? Type 'y' or 'n': ") == "y":
            continue_flag = True
            break
        else:
            print("Thanks for playing. Come again!")
            continue_flag = False
