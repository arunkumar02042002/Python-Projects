'''
Image-Downloader - A Python script that downloads an image when a URL is provided.
'''

# Import necessary libraries
import requests  # For making HTTP requests
import os  # For file and folder operations

def is_image_url(image_url: str) -> bool:
    # Send a HEAD request to the URL to check the Content-Type header
    response = requests.head(image_url)
    
    # Check if the Content-Type indicates an image (you can expand this list)
    return response.headers.get('Content-Type', '').startswith('image/')

    # Usage example:
    # if is_image_url(input_url):
    #     download_image(input_url, name=image_name, folder='images')
    # else:
    #     print('The provided URL does not lead to an image.')


# Define a function to find the extension from an image URL
def get_extension(image_url: str) -> str | None:

    if is_image_url(image_url):
        extensions: list[str] = ['.png', '.jpeg', '.jpg', '.gif', '.svg']
        for ext in extensions:
            if ext in image_url:
                return ext  # Return the extension if found in the URL
    else:
        raise Exception('The given URL does not lead to an image.')

# Define a function to download an image from a URL
def download_image(image_url: str, name: str, folder: str = None):

    # Attempt to obtain the file extension
    if ext := get_extension(image_url):
        if folder:
            # Define the image name with folder (if provided)
            image_name: str = f'{folder}/{name}{ext}'
        else:
            # Define the image name without a folder
            image_name: str = f'{name}{ext}'
    else:
        # Raise an exception if the extension is not found
        raise Exception('Image extension could not be located.')
    
    if os.path.isfile(image_name):
         # Raise an exception if the file name already exists
        raise Exception('File name already exists...')

    # Download Image
    try:
        # Make a GET request to the image URL and get its content
        image_content: bytes = requests.get(image_url).content
        with open(image_name, 'wb') as handler:
            # Write the image content to a file
            handler.write(image_content)
            print(f'Downloaded: "{image_name}" successfully!')
    except Exception as e:
        # Print an error message if any exception occurs
        print(f'Error: {e}')

# Entry point of the program
if __name__ == '__main__':
    input_url: str = input('Enter a URL: ')  # Prompt the user to enter a URL
    image_name: str = input('What would you like to name the image? ')  # Prompt for the desired image name

    print('Downloading.....')
    # Call the download_image function with the URL and image name
    download_image(input_url, name=image_name, folder='images')