import random
import os

def game(dif):
    user_lifes = 0

    if dif == "e":
        user_lifes = 10
    elif dif == "h":
        user_lifes = 5

    end_game = True
    random_num = random.randint(1, 100)
    while end_game:

        guess = int(input("Guess the number: "))

        if user_lifes != 0:

            if int(guess) == random_num:
                end_game = False
                print("Winner 🤩")
                play_again = input("Do you want to play again: ")
                if play_again == "y":
                    diffculty = input("Type 'h' for hard and 'e' for easy: ")
                    game(dif=diffculty)


            else:
                user_lifes -= 1
                print("Lives:", str(user_lifes))

                if int(guess) < random_num:
                    print("Too Low 👇") # Telling the user they must go higher

                elif int(guess) > random_num:
                    print("Too High 👆") # Telling the user they must go lower

        else:
            end_game = False
            print("You last. 😭")
            play_again = input("Do you want to play again: ")
            if play_again == "y":
                diffculty = input("Type 'h' for hard and 'e' for easy: ")
                game(dif=diffculty)





print(" ===== Number Guessing Game =====")


# Ask User which diffculty they want.
diffculty = input("Type 'h' for hard and 'e' for easy: ")

# Make a condition to handle they desired diffculty
game(dif=diffculty)




# Generate Random Number


# Ask user to make a guess


# Say if it is higher or lower then the actual number
