import smtplib
import os

# creates SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)

sender_email_id= os.getenv("EMAIL_ID")
receiver_email_id = input("receiver_email_id")
msg = input("msg")

# start TLS for security
s.starttls()

# Authentication
s.login(sender_email_id,"mlay ziug ywqz oytm")

# message to be sent
message = msg

# sending the mail
s.sendmail(sender_email_id, receiver_email_id, message)

# terminating the session
s.quit()
