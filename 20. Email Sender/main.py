'''
This script serves as a simple email sender that can be configured with your email address
and password to send emails with optional image attachments to recipients.
It is useful for sending basic email messages with attachments.
'''

# Import necessary libraries for sending emails and working with attachments.
import smtplib, ssl
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Import typing and dotenv to define constants and load environment variables.
from typing import Final
from dotenv import load_dotenv
import os

# Load environment variables from a .env file in the current directory.
load_dotenv()

# Define constants for email and password from environment variables.
EMAIL: Final[str] = os.getenv('EMAIL')
PASSWORD: Final[str] = os.getenv('PASSWORD')

# Function to create an image attachment from a file path.
def create_image_attachment(path: str) -> MIMEImage:
    with open(path, 'rb') as image:
        mime_image = MIMEImage(image.read())
        mime_image.add_header('Content-Disposition', f'attachment; filename={path}')
        return mime_image

# Function to send an email with optional image attachment.
def send_email(to_email: str, subject: str, body: str, image: str | None = None):
    host: str = 'smtp-mail.outlook.com'  # SMTP server hostname
    port: int = 587  # SMTP server port number

    context = ssl.create_default_context()

    # Connect to the SMTP server using a secure connection.
    with smtplib.SMTP(host, port) as server:
        print('Logging in....')
        server.ehlo()
        server.starttls(context=context)
        server.ehlo()

        # Log in to the SMTP server using the provided email and password.
        server.login(EMAIL, PASSWORD)

        # Prepare the email message.
        print('Trying to send an email....')
        message = MIMEMultipart()
        message['From'] = EMAIL
        message['To'] = to_email
        message['Subject'] = subject
        message.attach(MIMEText(body, 'plain'))

        if image:
            # If an image file is provided, create an attachment and add it to the email.
            file: MIMEImage = create_image_attachment(image)
            message.attach(file)

        # Send the email using the SMTP server.
        server.sendmail(from_addr=EMAIL, to_addrs=to_email, msg=message.as_string())

        # Print a success message after the email is sent.
        print('Sent!')

if __name__ == '__main__':
    # Example usage: Send an email with a subject, body, and an optional image attachment.
    send_email(
        to_email='arun.kumar.2403gg@gmail.com',
        subject='Hey buddy!',
        body='''Hello Buddy,
I have sent you an image of a cat.

Thanks!''',
        image='cat.png'
    )
