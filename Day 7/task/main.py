import random
import hangman_words
import hangman_art

def print_placeholder():
    print("".join(placeholder))

# TODO-1: - Update the word list to use the 'word_list' from hangman_words.py

lives = 6

# TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.
stages = hangman_art.stages
chosen_word = random.choice(hangman_words.word_list)
print(chosen_word)

placeholder = []
word_length = len(chosen_word)
for position in range(word_length):
    placeholder.append("_")
print_placeholder()


while "_" in placeholder and lives > 0:

    # TODO-6: - Update the code below to tell the user how many lives they have left.
    guess = input(f"Total lives: {lives}, Guess a letter:  ").lower()

    # TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in placeholder:
        print(f"you already choose this letter: {guess}")
    else:
        i = 0
        while i < len(chosen_word):
            if chosen_word[i] == guess:
                placeholder[i] = guess
            i += 1
        print_placeholder()
        if guess not in placeholder:
            # TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
            #  e.g. You guessed d, that's not in the word. You lose a life.
            lives -= 1
            print(f"Wrong guess, lives remaining  {lives}")
            print(stages[lives])

    if "_" not in placeholder:
        print("You win.")
    if lives == 0:
        print("You lost.")
