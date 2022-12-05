import datetime as _dt

import pydantic as _pydantic


class _BaseUserInfo(_pydantic.BaseModel):
    lastName: str
    firstName: str
    patronymic: str
    telephone: str
    message: str


class CreateUserInfo(_BaseUserInfo):
    pass


class UserInfo(_BaseUserInfo):
    id: int
    date_created: _dt.datetime

    class Config:
        orm_mode = True
