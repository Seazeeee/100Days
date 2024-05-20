import random
import hangman_art
import hangman_word


end_game = False


display = []

word_list = hangman_word.word_list

chosen_word = word_list[random.randint(0, len(word_list) - 1)]

lives = 6

# Testing code
print(f"Pssst, the solution is {chosen_word}.")

for _ in chosen_word:
    display.append("_")

print(hangman_art.logo)

while not end_game:
    guess = str(input("Please guess a letter: ")).lower()

    if guess in display:
        print(f"You have already entered {guess}, please try again.")
        print(" ".join(display))
        continue

    count = 0
    loose_life = False

    # TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.

    for char in chosen_word:
        count += 1
        if char == guess:
            display[count - 1] = guess

    if guess not in chosen_word:
        lives -= 1
        print(f"{guess} is not in the word. Try again.")
        if lives == 0:
            print("You lose.")
            end_game = True

    if "_" not in display:
        print("You win!")
        end_game = True

    print(" ".join(display))
    print(hangman_art.stages[lives])

print(f"The word was {chosen_word}.")
