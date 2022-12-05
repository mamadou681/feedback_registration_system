from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from credentials import Credentials
# Create database url
# {Credentials.db_host}:{Credentials.db_port}
part_url = f"{Credentials.db_username}:{Credentials.db_password}@db/{Credentials.db_name}"
DATABASE_URL = "postgresql://" + part_url
print(DATABASE_URL)
# Create the engine
engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
