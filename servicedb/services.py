from sqlalchemy.orm import Session

from database import Base, engine, SessionLocal
from models import UserInfo
from schema import CreateUserInfo, Userinfo


def add_table():
    return Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def create_userinfo(db: Session, userinfo: CreateUserInfo):
    userinfo = UserInfo(**userinfo)
    db.add(userinfo)
    db.commit()
    db.refresh(userinfo)
    return Userinfo.from_orm(userinfo)
