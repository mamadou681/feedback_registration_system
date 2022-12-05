import datetime as _dt
from sqlalchemy import Column, String, DateTime, Integer


from database import Base


class UserInfo(Base):
    __tablename__ = "userinfo"
    id = Column(Integer, primary_key=True, index=True)
    lastName = Column(String, index=True)
    firstName = Column(String, index=True)
    patronymic = Column(String, index=True)
    telephone = Column(String, index=True)
    message = Column(String, index=True)
    date_created = Column(DateTime, default=_dt.datetime.utcnow)
