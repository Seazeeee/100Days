############### Blackjack Project #####################

# Difficulty Normal 😎: Use all Hints below to complete the project.
# Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
# Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
# Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The the Ace can count as 11 or 1.
# Use the following list as the deck of cards:
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.
# The computer is the dealer.

##################### Hints #####################


# Hint 1: Go to this website and try out the Blackjack game:
#   https://games.washingtonpost.com/games/blackjack/
from art import logo
import random


def get_starter_cards():
    """Generates the starter cards for player.

    Returns:
        card1: First Card Selection
        card2: Second Card Selection
        total: The running sum of both cards
    """
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    card1 = cards[random.randint(0, len(cards) - 1)]

    card2 = cards[random.randint(0, len(cards) - 1)]

    total = card1 + card2

    return card1, card2, total


def get_card():
    """Gets a random card

    Returns:
        card1: A random card selection
    """
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    card1 = cards[random.randint(0, len(cards) - 1)]

    return card1


def aces(user_card1, user_card2):
    """Check for aces in players card. Resets that card to 1 if the player wants to split. Flags if there is only one 11.

    Args:
        user_card1 (int): Generated card1 from get_starter_cards()
        user_card2 (int): Generated card2 from get_starter_cards()

    Returns:
        user_card1 (int): The changed/unchanged card1
        user_card2 (int): The changed/unchanged card2
        True/False: The flag for aces
    """
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
    """Creates a card list that houses a dictionary for user and computer with their associated cards.

    Returns:
        card_list (list): A list of dictionaries for both user and dealer that tracks their current cards
        user_total (int): The total for user's cards
        dealer_total (int): The total for dealer's cards
    """
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
    """
    A function that plays blackjack and allows the user to hit or not hit. Checks the total for those cards. Then, ask if they user would like to play another game.
    """

    hit_question = True
    aces = ace_check
    recursion_total_user = user_total
    recursion_total_dealer = dealer_total

    while hit_question:
        if input("Type 'y' to get another card, type 'n' to pass: \n") == "y":
            new_card = get_card()
            card_list[0]["user"].append(new_card)
            recursion_total_user = sum(card_list[0]["user"])

            if sum(card_list[-1]["computer"]) < 17:
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
                if aces:
                    for num in card_list[0]["user"]:
                        if num == 11:
                            get_index = card_list[0]["user"].index(num)
                            card_list[0]["user"][get_index] = 1
                            recursion_total_user = sum(card_list[0]["user"])
                            aces = False
                            print("You went over 21!")
                            print(
                                f"Your new card hand is: {card_list[0]['user']}, current score: {recursion_total_user}"
                            )
                            print(
                                f"Computers hand:  {card_list[-1]['computer']}, current score: {recursion_total_dealer}"
                            )
                            break
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
                            break

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

            recursion_total_user = sum(card_list[0]["user"])
            recursion_total_dealer = sum(card_list[-1]["computer"])

            while sum(card_list[-1]["computer"]) < 17:
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
                            break
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
