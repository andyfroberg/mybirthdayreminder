from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    birthdays = relationship("Birthday", back_populates="owner")


class Birthday(Base):
    __tablename__ = "birthdays"

    id = Column(Integer, primary_key=True)
    birthday_name = Column(String, index=True)
    birthday_month = Column(String, index=True)
    birhtday_day = Column(Integer, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="birthdays")