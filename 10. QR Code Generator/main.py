# Import the qrcode library for generating QR codes
import qrcode

# Define a QR class for creating and customizing QR codes
class QR:
    def __init__(self, size: int, padding: int) -> None:
        # Initialize a QRCode object with the specified box size and border padding
        self.qr = qrcode.QRCode(box_size=size, border=padding)

    # Function to create a QR code with user-defined text/url, foreground, and background colors
    def create_qr(self, file_name: str, fg: str, bg: str):
        user_input = input('Enter text/url: ')  # Prompt the user to input text or a URL

        try:
            # Add the user input data to the QRCode object
            self.qr.add_data(user_input)

            # Generate the QR code image with specified foreground and background colors
            qr_image = self.qr.make_image(fill_color=fg, back_color=bg)

            # Save the QR code image in the current directory with the specified file name
            file_path = f'./10. QR Code Generator/{file_name}'
            qr_image.save(file_path)

            print(f'Successfully Created! ({file_name})')  # Print a success message

        except Exception as e:
            print(f'Error: {e}')  # Print an error message if an exception occurs

# Define the main function
def main():
    myqr = QR(size=30, padding=3)  # Create an instance of the QR class with specified size and padding
    myqr.create_qr('qr.png', fg='black', bg='white')  # Generate a QR code with custom colors and save it as 'qr.png'

# Entry point of the program
if __name__ == '__main__':
    main()  # Call the main function when the script is run