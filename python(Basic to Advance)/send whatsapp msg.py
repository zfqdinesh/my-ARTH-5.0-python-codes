import pywhatkit as kit

# Phone number with country code (e.g., +1 for the US, +91 for India)
phone_number = input("+911234567891  use this type of number those you want to msg    now enter:-     ")

# Message you want to send
message = input("enter your msg")

# Send the message instantly
kit.sendwhatmsg_instantly(phone_number, message)

print("Message sent successfully!")
