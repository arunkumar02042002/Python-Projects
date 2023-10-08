# Import necessary libraries
import string
import secrets

# Function to check if the password contains uppercase characters
def containsUpper(password: str) -> bool:
    for char in password:
        if char.isupper():
            return True
    return False

# Function to check if the password contains punctuation symbols
def containsPunctuation(password: str) -> bool:
    for char in password:
        if char in set(string.punctuation):
            return True
    return False

# Function to generate a password based on given constraints
def generatePassword(length: int, symbols: bool, uppercase: bool) -> str:
    # Define the character combination for the password
    combination: str = string.ascii_lowercase + string.digits

    # Include symbols if specified
    if symbols:
        combination += string.punctuation
        
    # Include uppercase characters if specified
    if uppercase:
        combination += string.ascii_uppercase
    
    combination_length = len(combination)
    password = ''

    # Generate the password
    for _ in range(length):
        password += combination[secrets.randbelow(combination_length)]

    return password

if __name__ == '__main__':
    # Get the number of passwords to generate
    n = int(input('How many passwords do you want to generate? '))

    for i in range(1, n+1):
        print('----------------------------------------------------------------------------------------------------------')
        print(f"Enter constraints for your {i}th password!")

        # Get the desired password length
        length: int = int(input("Enter the length of the password: "))
        while length < 8:
            length = int(input("Length must be greater than 7: "))

        symbols: bool = False
        uppercase: bool = False

        # Check if the user wants to include symbols
        if input("Do you want to include symbols (y/n)? ") == 'y':
            symbols = True

        # Check if the user wants to include uppercase characters
        if input("Do you want to include uppercase characters (y/n)? ") == 'y':
            uppercase = True

        # Generate the password based on constraints
        my_password: str = generatePassword(length, symbols, uppercase)

        # Ensure the password meets specified constraints
        if symbols == True and containsPunctuation(my_password) == False:
            my_password = generatePassword(length, symbols, uppercase)

        if uppercase == True and containsUpper(my_password) == False:
            my_password = generatePassword(length, symbols, uppercase)

        # Print the generated password and its specifications
        print(f'Your Password -> {my_password} (Specifications: Contains Uppercase: {uppercase}, Contains symbols: {symbols})')
        print('----------------------------------------------------------------------------------------------------------')