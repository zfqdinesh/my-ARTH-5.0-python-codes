from instagrapi import Client
import os

# Initialize the Instagram client
client = Client()

# Log in to your Instagram account
username = os.getenv('INSTA_username')
password = os.getenv('INSTA_password')
x=5
print({username},  {password})
client.login(username, password)

# # Define the photo and caption
photo_path = input(" enter file path like this        C:/Users/Dell/OneDrive/Documents/Downloads/instagram post.webp")
caption = input("enter your tytle and tags   ")

# Post the photo
client.photo_upload(photo_path, caption)
