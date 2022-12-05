import sqlalchemy as _sql
import sqlalchemy.ext.declarative as _declarative
import sqlalchemy.orm as _orm

from credentials import Credentials
# Create database url
# {Credentials.db_host}:{Credentials.db_port}
part_url = f"{Credentials.db_username}:{Credentials.db_password}@db/{Credentials.db_name}"
DATABASE_URL = "postgresql://" + part_url
print(DATABASE_URL)
# Create the engine
engine = _sql.create_engine(DATABASE_URL)

SessionLocal = _orm.sessionmaker(
    autocommit=False, autoflush=False, bind=engine)

Base = _declarative.declarative_base()
