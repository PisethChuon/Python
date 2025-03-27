# SMTP.py

`SMTP.py` is a Python script that allows you to send emails using the Simple Mail Transfer Protocol (SMTP). This script can be used to automate email sending for various purposes such as notifications, alerts, or regular updates.

## Features

- Send emails using SMTP
- Support for multiple recipients
- Attachments support
- Customizable email subject and body

## Requirements

- Python 3.x
- `smtplib` (included in the Python Standard Library)
- `email` (included in the Python Standard Library)

## Usage

1. Clone the repository or download the `SMTP.py` file.
2. Open the `SMTP.py` file and configure the SMTP server settings, sender email, and recipient email addresses.
3. Run the script using Python:

    ```bash
    python SMTP.py
    ```

## Configuration

Edit the following variables in the `SMTP.py` file to match your email server settings and email details:

```python
smtp_server = 'smtp.example.com'
smtp_port = 587
sender_email = 'your-email@example.com'
sender_password = 'your-email-password'
recipient_emails = ['recipient1@example.com', 'recipient2@example.com']
subject = 'Your Email Subject'
body = 'Your email body text goes here.'
```

## Example

Here is an example of how to use the `SMTP.py` script:

```python
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# SMTP server configuration
smtp_server = 'smtp.example.com'
smtp_port = 587
sender_email = 'your-email@example.com'
sender_password = 'your-email-password'
recipient_emails = ['recipient1@example.com', 'recipient2@example.com']

# Email content
subject = 'Your Email Subject'
body = 'Your email body text goes here.'

# Create the email message
msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = ', '.join(recipient_emails)
msg['Subject'] = subject
msg.attach(MIMEText(body, 'plain'))

# Send the email
try:
     server = smtplib.SMTP(smtp_server, smtp_port)
     server.starttls()
     server.login(sender_email, sender_password)
     text = msg.as_string()
     server.sendmail(sender_email, recipient_emails, text)
     server.quit()
     print('Email sent successfully!')
except Exception as e:
     print(f'Failed to send email: {e}')
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## Contact

For any questions or inquiries, please contact [your-email@example.com](mailto:your-email@example.com).
