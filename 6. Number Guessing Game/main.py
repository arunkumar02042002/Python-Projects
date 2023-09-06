from random import randrange

# Global variables
ATTEMPTS = 7
computer_guess = randrange(1, 100)
USER_MIN = 0
USER_MAX = 100

print("Guess a number between 1 to 100:")
print(f"Your total number of attempts: {ATTEMPTS}")
print("--------------------------------------------")

while(ATTEMPTS):
    try:
        user_guess = int(input("Enter your guess: "))
        if user_guess == computer_guess:
            print("Woo Hoo! You Guess The Right Number.")
            break
        else:
            ATTEMPTS -= 1
            print(f"Attempts Left: {ATTEMPTS}:")
            
            if user_guess < computer_guess:
                USER_MIN = max(USER_MIN, user_guess)
                print(f"Guess a number greater than {USER_MIN} and smaller than {USER_MAX}.")
            else:
                USER_MAX = min(USER_MAX, user_guess)
                print(f"Guess a number smaller than {USER_MAX} and greater than {USER_MIN}.")
            print("--------------------------------------------")
    except:
        print("Enter a valid number!")
        print("--------------------------------------------")

else:
  print(f"Computer Guessed {computer_guess}. Sorry for your loss!")