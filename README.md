**Bulk Email Sender**

This script allows you to send personalized bulk emails using Gmail. It reads recipient details from a CSV file and sends emails using the Gmail SMTP server.

**Features**

1. Reads recipient names and emails from a CSV file
2. Sends personalized emails using a pre-defined template
3. Uses Gmail SMTP for sending emails

**Prerequisites**

1. A Gmail account with App Password (if 2FA is enabled)
2. Python installed on your system
3. Required libraries: smtplib, csv, email.mime

**Installation**

1. Clone or download this repository.
2. Install required dependencies (if not already available):
3. pip install email
4. Ensure your recipients.csv file is in the same directory as the script.

**CSV Format**

The recipients.csv file should be formatted as follows:

NAME,EMAIL
John Doe,john.doe@example.com
Alice Smith,alice.smith@gmail.com

**Configuration**

1. Set Your Gmail Credentials
Replace the following placeholders in the script:

GMAIL_USER = "your-email@gmail.com"
GMAIL_PASSWORD = "your-app-password"
⚠️ Do not use your actual password. Generate an App Password from your Google account settings if 2FA is enabled.

2. **Customize Email Subject & Body**
Modify the SUBJECT and BODY variables in the script:

SUBJECT = "Your Subject Here"
BODY = """Dear {name}, 
I hope this email finds you well.  
...
Best regards,  
Your Name  
"""
Use {name} as a placeholder to personalize the recipient's name.

**Running the Script**

Run the script using Python:
python bulk_mailer.py
The script will read recipient details from the CSV and send personalized emails.

**Troubleshooting**

1. Emails going to spam?
Avoid spam-triggering words in the subject and body.
Use a professional email address.
2. Authentication errors?
Enable Less Secure Apps in your Google account.
Use an App Password if 2FA is enabled.
3. SMTP Connection Issues?
Ensure port 587 is open on your network.
Try running the script with a VPN if facing connection issues.

**Disclaimer**

This script is for educational purposes only. Sending bulk unsolicited emails can violate email service provider policies. Always ensure compliance with anti-spam regulations.
