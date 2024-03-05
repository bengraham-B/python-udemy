import random
import os

user_cards = []
pc_cards = []
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_cards():
    user_cards.append(cards[random.randint(1, len(cards)) - 1])
    pc_cards.append(cards[random.randint(1, len(cards)) - 1])

def check_21(array):
    sum = 0
    for n in array:
        sum += n

    if sum >= 21:
        return True

def check_who_wins(array):
    sum = 0
    for n in array:
        sum += n

    return 21 - sum


# ========= Game Loop =========
deal_cards()
print("Your Cards", user_cards)
print("PC Cards", pc_cards)

continue_game = True
while continue_game == True:

    hit = input("Hit: ")

    if hit == "y":
        os.system('clear')
        deal_cards()

        if check_21(user_cards) == True:
           print("User Won")
           continue_game = False


        if check_21(pc_cards) == True:
            print("PC Won")
            continue_game = False

        print("Your Cards: ", user_cards)

    else:
        os.system("clear")
        print("Your Cards", user_cards)
        print("PC Cards", pc_cards)

        if check_21(user_cards) == True:
           print("User Won")
           continue_game = False


        if check_21(pc_cards) == True:
            print("PC Won")
            continue_game = False

        if check_who_wins(user_cards) > check_who_wins(pc_cards):
            print("user Wins")
            continue_game = False

        if check_who_wins(user_cards) < check_who_wins(pc_cards):
            print("user Wins")
            continue_game = False
