from typing import TYPE_CHECKING

import database as _database
import models as _models
from sqlalchemy.orm import Session

import schema as _schema


def add_table():
    return _database.Base.metadata.create_all(bind=_database.engine)


def get_db():
    db = _database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


def create_userinfo(db: Session, userinfo: _schema.CreateUserInfo):
    userinfo = _models.UserInfo(**userinfo)
    db.add(userinfo)
    db.commit()
    db.refresh(userinfo)
    return _schema.UserInfo.from_orm(userinfo)
