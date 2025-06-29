# Copyright 2025 ( @annuaicoder )
# Send a basic email via Gmail SMTP.

import smtplib

sender = "you@gmail.com"
password = "your_app_password"
receiver = "target@example.com"

with smtplib.SMTP("smtp.gmail.com", 587) as server:
    server.starttls()
    server.login(sender, password)
    msg = "Subject: Test\n\nThis is a test email from Python!"
    server.sendmail(sender, receiver, msg)
