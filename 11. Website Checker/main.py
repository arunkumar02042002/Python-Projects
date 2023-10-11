# Import necessary libraries and modules
import csv
import requests
from fake_useragent import UserAgent
from http import HTTPStatus

# Define a function to extract websites from a CSV file and format their URLs
def getWebsite(csv_file: str) -> list[str]:
    websites: list[str] = []
    with open(csv_file, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            if 'https://' not in row[1] or 'http://' not in row[1]:
                websites.append(f'https://{row[1]}')
            else:
                websites.append(row[1])
    return websites

# Define a function to retrieve a user agent for making HTTP requests
def get_useragent() -> str:
    ua = UserAgent()  # Initialize a UserAgent object
    return ua.chrome  # Get a Chrome user agent string

# Define a function to get the description of an HTTP status code
def get_status_description(status_code: int) -> str:
    for value in HTTPStatus:  # Iterate through HTTPStatus enum
        if value == status_code:  # Check if the status code matches the enum value
            description: str = f'({value} {value.name}) {value.description}'
            return description  # Return the status description if found
    return '??? Unknown status code...'  # Return this message if the status code is not found

# Define a function to check the status of a website and print the result
def check_website(website: str, user_agent):
    try:
        code: int = requests.get(website, headers={'User-Agent': user_agent}).status_code
        # Send an HTTP GET request to the website with the specified user agent
        print(website, get_status_description(code))  # Print the website URL and its status description
    except Exception:
        print(f'Could not find any information for website: {website}')

# Define the main program logic
def main():
    sites: list[str] = getWebsite('website.csv')  # Get the websites from the CSV file
    user_agent: str = get_useragent()  # Get a user agent string

    for site in sites:
        check_website(site, user_agent)  # Check the status of each website using the user agent

# Entry point of the program
if __name__ == '__main__':
    main()  # Call the main function when the script is run
