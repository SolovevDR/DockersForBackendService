from sqlalchemy import (
    Column, Integer, String, DateTime, BOOLEAN, ARRAY, Float, ForeignKey
)
from datetime import datetime

from sqlalchemy.dialects.postgresql import BYTEA
from sqlalchemy.orm import relationship

from database import Base


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=True)
    login = Column(String)
    password = Column(String)
    comment = Column(String, nullable=True)
    role = Column(Integer, ForeignKey("role.id"))

    role_id = relationship("Role", back_populates="owner")


class Role(Base):
    __tablename__ = "role"

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String, nullable=False)

    owner = relationship("User", back_populates="role_id")
