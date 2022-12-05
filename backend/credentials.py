from os import environ as env

from dotenv import find_dotenv, load_dotenv

#Search for a .env file
path = find_dotenv()

# take environment variables from .env.
load_dotenv(path, verbose=True)

# Get the username and password from actual environment
username = env.get("RABBITMQ_USERNAME")
password = env.get("RABBITMQ_PASSWORD")