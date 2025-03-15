Bulk Email Sender

This script allows you to send personalized bulk emails using Gmail. It reads recipient details from a CSV file and sends emails using the Gmail SMTP server.

Features

Reads recipient names and emails from a CSV file
Sends personalized emails using a pre-defined template
Uses Gmail SMTP for sending emails
Prerequisites

A Gmail account with App Password (if 2FA is enabled)
Python installed on your system
Required libraries: smtplib, csv, email.mime
Installation

Clone or download this repository.
Install required dependencies (if not already available):
pip install email
Ensure your recipients.csv file is in the same directory as the script.
CSV Format

The recipients.csv file should be formatted as follows:

NAME,EMAIL
John Doe,john.doe@example.com
Alice Smith,alice.smith@gmail.com
Configuration

1. Set Your Gmail Credentials
Replace the following placeholders in the script:

GMAIL_USER = "your-email@gmail.com"
GMAIL_PASSWORD = "your-app-password"
⚠️ Do not use your actual password. Generate an App Password from your Google account settings if 2FA is enabled.
2. Customize Email Subject & Body
Modify the SUBJECT and BODY variables in the script:

SUBJECT = "Your Subject Here"
BODY = """Dear {name}, 
I hope this email finds you well.  
...
Best regards,  
Your Name  
"""
Use {name} as a placeholder to personalize the recipient's name.

Running the Script

Run the script using Python:

python bulk_email_sender.py
The script will read recipient details from the CSV and send personalized emails.

Troubleshooting

Emails going to spam?
Avoid spam-triggering words in the subject and body.
Use a professional email address.
Authentication errors?
Enable Less Secure Apps in your Google account.
Use an App Password if 2FA is enabled.
SMTP Connection Issues?
Ensure port 587 is open on your network.
Try running the script with a VPN if facing connection issues.
Disclaimer

This script is for educational purposes only. Sending bulk unsolicited emails can violate email service provider policies. Always ensure compliance with anti-spam regulations.
