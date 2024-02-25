#Step 1
import random

word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
random_int = (random.randint(1, len(word_list))) - 1
choose_word = word_list[random_int]
print(choose_word)

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess = (input("Enter a letter: ").lower())
if len(guess) > 1:
    print("Please only guess one letter at a time")

print(guess)

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
for i in range(0, len(choose_word) -1):
    if choose_word[i] == guess:
        print("YES")
    else:
        print("NO")
