from os import environ as env
from dotenv import find_dotenv, load_dotenv

# Search for a .env file
path = find_dotenv()

# take environment variables from .env.
load_dotenv(path, verbose=True)


class Credentials:
    # Get db config from actual environment
    db_username: str = env.get("DATABASE_USERNAME")
    db_password: str = env.get("DATABASE_PASSWORD")
    db_port: int = env.get("POSTGRES_PORT", default=5432)
    db_host: str = env.get("POSTGRES_HOST")
    db_name: str = env.get("DATABASE_NAME")
    # Get the username and password from actual environment
    username: str = env.get("RABBITMQ_USERNAME")
    password: str = env.get("RABBITMQ_PASSWORD")
