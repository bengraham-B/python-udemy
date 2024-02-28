import os
from art import logo
exit_program = False

all_bids = []

def add_bid(name, amount):
    new_bid = {
        "name": name,
        "bid_amount": amount
    }

    all_bids.append(new_bid)

def highest_bidder(bids_array):
    highest_amount = 0
    name = ""

    for key in bids_array:
        if int(key["bid_amount"]) > highest_amount:
            highest_amount = int(key["bid_amount"])
            name = key["name"]

    print(f"The winner is {name} with a bid of ${str(highest_amount)}")

while exit_program != True:
    print(logo)
    print("Welcome to the slient Acuction Program")
    name = input("What is your name: ")
    bid_amount = input("What is your bid amount($): ")

    add_bid(name, bid_amount)

    any_other_bids = input("Are there any other bidders? Yes or No: ")

    end_phrases = ["no", "No", "n", "nope", "Nope", "Nah", "end", "exit"]

    if any_other_bids in end_phrases:
        os.system('clear')
        highest_bidder(all_bids)
        exit_program = True

    else:
        os.system('clear')
