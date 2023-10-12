'''
Common Password Chexker is a Python script that can check how common a password is!
'''

# Define a function to check if a password is common
def check_password(password: str):
    with open('top_common_passwords.txt', 'r') as file:
        # Read a list of common passwords from a text file and store them as a dictionary
        common_passwords = {}
        rank = 1
        for i in file.read().splitlines():
            common_passwords[i] = rank
            rank += 1

        if password in common_passwords:
            # Check if the input password is in the dictionary of common passwords
            print(f'{password} (\u274c) : Your password is too common. It is in top {common_passwords[password]} common passwords!')
        else:
            print(f'{password} (\u2713) : Hurrah! You have chosen a unique password.')

# Define the main program logic
def main():
    while True:
        password: str = input('Enter Your Password: ')  # Prompt the user to enter a password

        # Minimum length requirement
        if len(password) >= 4:
            # Call the check_password function to evaluate the password
            check_password(password)
            break
        else:
            print("Password should contain at least four characters.")

# Entry point of the program
if __name__ == '__main__':
    main()  # Call the main function when the script is run