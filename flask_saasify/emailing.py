import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from flask import render_template

import os


def send_email(html, to, subject):
    # Email setup
    sender_email = os.environ.get("EMAIL_SMTP_SENDER_EMAIL")
    sender_name = os.environ.get("EMAIL_SMTP_SENDER_NAME")
    receiver_email = to
    password = os.environ.get("EMAIL_SMTP_PASSWORD")

    # Create message container
    msg = MIMEMultipart("alternative")
    msg["Subject"] = subject
    msg["From"] = f"{sender_name} <{sender_email}>"
    msg["To"] = receiver_email

    # Record the MIME types
    part2 = MIMEText(html, "html")

    # Attach parts into message container
    msg.attach(part2)

    # Send the message via local SMTP server
    with smtplib.SMTP(os.environ.get("EMAIL_SMTP_SERVER"), 587) as server:
        server.starttls()  # Secure the connection
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
