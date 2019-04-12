#! /usr/bin/env python

import smtplib

# Create smtp Object to Gmail on port 587
smtpObj = smtplib.SMTP('smtp.gmail.com', 587)

# Check the object type
print(type(smtpObj))

# Send a message to the server to check status
print(smtpObj.ehlo())

# Start TLS encryption
print(smtpObj.starttls())

# Login/password
print(smtpObj.login('youremailaddress@gmail.com', 'password'))

# Collect Email address to send to
recipient = input("To: ")

# Subject
subject = input("Subject: ")

# Body
text_body = input("Message: ")

# Send Email
smtpObj.sendmail('youremailaddress@gmail.com', recipient, 'Subject: ' + subject +'\n' + text_body)

# Done
print("Sent!")

# Quit smtp process
smtpObj.quit()
