import datetime as _dt
from pydantic import BaseModel


class _BaseUserInfo(BaseModel):
    lastName: str
    firstName: str
    patronymic: str
    telephone: str
    message: str


class CreateUserInfo(_BaseUserInfo):
    pass


class Userinfo(_BaseUserInfo):
    id: int
    date_created: _dt.datetime

    class Config:
        orm_mode = True
