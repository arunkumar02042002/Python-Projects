'''
Password-Predictor is a Python script that brute forces a word, password, or any type of text.
'''

# Import necessary libraries
import time
import itertools
import string 

# Define a decorator to measure the time taken by a function
def time_taken(func):
    def timee(*args, **kwargs):
        start_time = time.perf_counter()  # Record the start time
        result = func(*args, **kwargs)  # Execute the wrapped function
        end_time = time.perf_counter()  # Record the end time

        # Return the result of the wrapped function along with the execution time
        return result + f'\nTotal time taken to guess your password: {round(end_time - start_time, 2)}s'
    return timee

# Define a brute-force function to predict a password
@time_taken  # Apply the time_taken decorator to measure execution time
def brute_force(password: str, length: int, uppercase: bool = False, digits: bool = False, symbols: bool = False) -> str | None:
    characters: str = string.ascii_lowercase

    if uppercase:
        characters += string.ascii_uppercase

    if digits:
        characters += string.digits

    if symbols:
        characters += string.punctuation

    # Initialize the count of password attempts
    attempts: int = 0  

    for i in itertools.product(characters, repeat=length):
        guess: str = ''.join(i)  # Generate a guess by joining characters
        attempts += 1

        # Return if the password is found
        if guess == password:
            return f'{password} : was cracked in {attempts:,} attempts.'

# Define a function to check if a password is in the common password list
def check_in_common_password(password: str) -> str | None:
    with open('common_passwords.txt', 'r') as file:
        # Read common passwords from a file and store them as a set
        common_passwords = set(file.read().splitlines())

        if password in common_passwords:
            # Return if the password is common
            return f'{password} : is a common password used by millions of others.'

# Define the main function for executing the program
def main():
    print('Searching.....')
    password: str = 'apple'

    # Check if the password is in the common passwords list
    if match := check_in_common_password(password):
        print(match)
    else:
        # If not common, attempt to brute force the password
        if match := brute_force(password, 5): 
            print(match)
        else:
            print("Can't crack!")

# Entry point of the program
if __name__ == '__main__':
    main()  # Execute the main function when the script is run