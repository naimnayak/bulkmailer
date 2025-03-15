import smtplib
import csv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Gmail Credentials
GMAIL_USER = "" # Enter your email
GMAIL_PASSWORD = ""  # Use an App Password if 2FA is enabled

# Email Subject & Body Template
SUBJECT = "" #Enter your subject here 

#Replace with your actual mail, use spam free words to avoid getting your mail into spam folder 

BODY = """Dear {name}, 


I hope this email finds you well.  

I am reaching out to [briefly state the purpose of the email, e.g., introduce yourself, offer a service, request information, etc.].  

Here are some key details:  
- [Point 1]  
- [Point 2]  
- [Point 3]  

Please let me know your thoughts, and feel free to ask any questions. I’d be happy to discuss this further at your convenience.  

Looking forward to your response.  

Best regards,  
[Your Name]  
[Your Company/Organization (if applicable)]  
[Your Contact Information]  
[Your Email Signature (if applicable)] 
  
"""

# Read Recipients from CSV File
# Replace the demo csv with your actual csv 
csv_file = "recipients.csv"  # Ensure this file is in the same directory
recipients = []
with open(csv_file, "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        recipients.append({
            "name": row["NAME"].strip(),
            "email": row["EMAIL"].strip()
        })

def send_email(to_email, name):
    """Send an email to a recipient"""
    msg = MIMEMultipart()
    msg["From"] = GMAIL_USER
    msg["To"] = to_email
    msg["Subject"] = SUBJECT

    # Personalize email body
    body = BODY.format(name=name)
    msg.attach(MIMEText(body, "plain"))

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(GMAIL_USER, GMAIL_PASSWORD)
        server.sendmail(GMAIL_USER, to_email, msg.as_string())
        server.quit()
        print(f"✅ Email sent to {name} ({to_email})")
    except Exception as e:
        print(f"❌ Failed to send email to {to_email}: {e}")

# Sending bulk emails
for recipient in recipients:
    send_email(recipient["email"], recipient["name"])
