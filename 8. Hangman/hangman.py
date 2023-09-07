# import the random python module to pick a random word from the hangman guessing words:
import random
from hangman_guessing import guess_dict

computer_guess = random.choice(list(guess_dict.keys())).lower()
word_letters = len(computer_guess)

game_over = False
tries = 6

#Testing your code:
print(f'The word you guessed is {computer_guess}.')


#Import the game name from hangman_life.py and print it at the game start:
from hangman_life import game_name
print(game_name)
print(f"This is a {word_letters} letters word.")
print(f"You have {tries} tries to guess the word. On each failed attempt you lose a try.")

#Create blank list called result to add right letters that the players have guessed to it:
result = []
for _ in range(word_letters):
    result += "_"

# iterate over the players input letters if the game not yet end:
while not game_over:
    print("-------------------------------------------------")
    user_guessing = input("Guess a letter or type 'hint' for hint: ").lower()

    if user_guessing.lower() == 'hint':
        print(f"Hint: {guess_dict[computer_guess.title()]} Starts with letter {computer_guess[0]}")
        continue
    # If the players enter a letter that they guessed, print the letter and let them know:
    if user_guessing in result:
        print(f"The letter you guess {user_guessing}")

    # Now check if the guessed letter is right or wrong
    for position in range(word_letters):
        letter = computer_guess[position]
        # Print the current oposition of the right letter that the players have guessed:
        if letter == user_guessing:
            result[position] = letter

    #Check if the players guess the wrong letter they will lose a try.
    if user_guessing not in computer_guess:
        tries -= 1
        #If the letter is not in the guessed_word, print out the letter and let them know it's not in the word.
        print(f"You guessed {user_guessing}, this letter is not in the word.")
        print(f"You lose a try. Tries Left: {tries}")

        # After the players lose all of their tries they will lose the game and  
        if tries == 0:
            game_over = True
            print("You Lose, Game Over.")
            print(f"Computer Guessed {computer_guess}")

    #Join all the elements in the result list and turn it into a String.
    print(f"{' '.join(result)}")

    #Check if the players has got all the right letters so they will win the game.
    if "_" not in result:
        game_over = True
        print("You are a winner, Congratulations.")

    # Import the lives from hangman_life.py module and make this error go away.
    from hangman_life import lives
    print(lives[tries])