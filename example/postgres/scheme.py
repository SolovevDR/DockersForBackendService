from typing import Optional, List

from pydantic import BaseModel


class OneUser(BaseModel):
    id: int
    login: str
    password: str
    comment: Optional[str]
    role_name: str

    class Config:
        from_attributes = True


class ListUsers(BaseModel):
    users: List[OneUser]


class OneRole(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True


class ListrRoles(BaseModel):
    roles: List[OneRole]
