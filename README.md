# Email Sender Script

This repository contains a Python script for sending emails automatically through SMTP. It's a simple and easy-to-use script that allows you to send emails from your Gmail account using Python.

## Features

- Send emails automatically through Gmail.
- Customize the recipient, subject, and body of the email.
- Can send to multiple recipients at once.

## Requirements

To use this script, you'll need to have the following:

- Python 3.x installed
- A Gmail account
- The following Python libraries (which can be installed via pip):
  ```bash
  pip install smtplib

## Usage

1. **Edit the script**:
   - In the `send_mail.py` script, replace the following variables with your information:
     - `YOUR_EMAIL`: Your Gmail email address.
     - `YOUR_PASSWORD`: Your Gmail app password.
     - `recipient_email`: The recipient’s email address.
     - `subject`: The subject of the email.
     - `body`: The body of the email.

2. **Run the script**:
   To run the script, use the following command in your terminal:
   ```bash
   python send_mail.py


## Note
### App Passwords: 
You need to generate an app password for your Gmail account (since Google blocks less secure apps). Follow this guide to generate one.

### Security: 
Be cautious while handling your email credentials. It's better to use environment variables or a secrets manager to keep your sensitive information safe.

## License
This project is licensed under the MIT License.
