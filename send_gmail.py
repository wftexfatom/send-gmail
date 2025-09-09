import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Email credentials and settings
gmail_user = 'your_email@gmail.com'
gmail_password = 'your_app_password'  # Use App Password if 2FA is enabled

# Email details
to = 'recipient@example.com'
subject = 'Test Email from Python'
body = 'Hello,\n\nThis is a test email sent from a Python script using Gmail SMTP.'

# Create the email message
msg = MIMEMultipart()
msg['From'] = gmail_user
msg['To'] = to
msg['Subject'] = subject
msg.attach(MIMEText(body, 'plain'))

try:
    # Connect to Gmail SMTP server
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(gmail_user, gmail_password)

    # Send the email
    server.sendmail(gmail_user, to, msg.as_string())
    print('Email sent successfully!')
except Exception as e:
    print(f'Error: {e}')
finally:
    server.quit()
