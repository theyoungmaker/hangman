import os
import random

from hangman_images import starting_image, lives_images, lose_image, win_image
from hangman_strings import word_list

is_game_over = False
num_lives = len(lives_images) - 1

# Step 1: Print the starting_image onto console when we start the game
print(starting_image)

# Step 2: Choose a word from word_list to be mystery word for hangman game
word_to_guess = random.choice(word_list)
# print(word_to_guess) # To be commented

# Step 3: Show clue to player
word_length = len(word_to_guess)
clue = []
for _ in range(word_length):
    clue.append("_")
print(" ".join(clue))

# Step 4: Get User to guess letter
while not is_game_over:
    guess = input("Guess a letter: ").lower()

    os.system("cls")

    while not len(guess) == 1 or not guess.isalpha():
        guess = input("Please give a valid letter: ").lower()

    # print(guess) # To be commented out

    # Step 5: Check if Letter guessed is in Mystery Word
    for index in range(word_length):
        letter = word_to_guess[index]
        if letter == guess:
            clue[index] = letter
    print(" ".join(clue))

    # Step 6: Check if Letter guessed is not in Mystery Word
    if guess not in word_to_guess:
        num_lives -= 1
        print("Oops! You guessed a wrong letter and you lose a life! :(")

    print(lives_images[num_lives])

    # Step 7: Check if Player won or lost
    if not "_" in clue:
        is_game_over = True
        print(win_image)

    if num_lives == 0:
        is_game_over = True
        print(lose_image)
        print("Oh no! You ran out of lives! The word is {}".format(word_to_guess))

# Enclose Steps 4 to 7 in while loop so long as game is not over
