from typing import Final
# Import the requests library for making HTTP requests
import requests

# Get your API key from here 'https://cutt.ly/'
API_KEY: Final[str] = '71adb130de327aa8c16c6f33e9d2c05821e1f'

# Base URL of the link shortening service
BASE_URL: Final[str] = 'https://cutt.ly/api/api.php'

# Define a function to shorten a given link
def shorten_link(full_link: str):
    # Create a dictionary with the API key and the full link to be shortened
    payload: dict = {
        'key': API_KEY,
        'short': full_link
    }

    # Send a GET request to the link shortening service
    request = requests.get(BASE_URL, params=payload)

    # Parse the response data as JSON
    data: dict = request.json()

    # Use a walrus operator to extract 'url_data' if it exists in the response
    if url_data := data.get('url'):

        # Check the 'status' field in the response
        # To know more about 'status' field visit 'https://cutt.ly/api-documentation/regular-api'
        match url_data['status']:
            case 1:
                print('The shortened link comes from the domain that shortens the link, i.e. the link has already been shortened.')
            case 2:
                print('The entered link is not a link.')
            case 3:
                print('The preferred link name is already taken.')
            case 4:
                print('Invalid API key.')
            case 5:
                print('The link has not passed the validation. Includes invalid characters.')
            case 6:
                print('The link provided is from a blocked domain.')
            case 7:
                # Extract the shortened link and print it
                short_link: str = url_data['shortLink']
                print(f'Link: {short_link}')
            case 8:
                print('You have reached your monthly link limit. You can upgrade your subscription plan to add more links.')
            case _:
                print(f"Error Status: {url_data['status']}")

# Main function to interact with the user
def main():
    # Prompt the user to enter a link
    input_link: str = input('Enter a link: ')
    
    # Call the 'shorten_link' function
    shorten_link(input_link)

if __name__ == '__main__':
    # Call the 'main' function to start the link shortening process
    main()