import datetime as _dt
import sqlalchemy as _sql


import database as _database


class UserInfo(_database.Base):
    __tablename__ = "userinfo"
    id = _sql.Column(_sql.Integer, primary_key=True, index=True)
    lastName = _sql.Column(_sql.String, index=True)
    firstName = _sql.Column(_sql.String, index=True)
    patronymic = _sql.Column(_sql.String, index=True)
    telephone = _sql.Column(_sql.String, index=True)
    message = _sql.Column(_sql.String, index=True)
    date_created = _sql.Column(_sql.DateTime, default=_dt.datetime.utcnow)
