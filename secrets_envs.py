# A simple way to handle secrets and environment variables without a centralized secret management system
# Also an easy way to load environment variables generally
#Ref: https://stackoverflow.com/questions/73642345/how-to-securely-pass-credentials-in-python

# NOTE - BE SURE TO EXCLUDE .env IN .gitignore!!!

import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv('fake_creds.env')) # Load the .env file.

# Fetch variables from the .env file.
account_username = os.getenv("ACCOUNT_USERNAME")
account_password = os.getenv("ACCOUNT_PASSWORD")

# examples stored in fake_creds.env

print(account_username, account_password)
