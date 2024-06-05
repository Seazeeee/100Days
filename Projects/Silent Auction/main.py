from art import logo
import os

# os.systems('clear")


def find_highest_bidder(bid_record):
    highest_amount = 0
    winner = ""

    highest_amount = max(bid_record.values())

    for key, val in bidders_info.items():
        if val == highest_amount:
            winner = key

    print(f"The winner is {winner} with a bid of ${highest_amount}.")


def add_bid_info():
    user_name = str(input("What is your name?: "))
    bid_amount = float(input("What's your bid?: $"))

    bidders_info[user_name] = bid_amount


print(logo)
print("Welcome to the secret auction program.")
bidding_finished = False

bidders_info = {}

while not bidding_finished:
    add_bid_info()
    more_bids_question = str(
        input("Are there any other bidders? Type 'yes' or 'no'. \n")
    ).lower()

    if more_bids_question == "yes" or more_bids_question == "y":
        os.system("clear")
        print(f"This is the current dictionary: \n{bidders_info}")
        continue
    else:
        find_highest_bidder(bid_record=bidders_info)
        bidding_finished = True
