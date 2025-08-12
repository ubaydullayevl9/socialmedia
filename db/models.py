from sqlalchemy import (Integer, Column, String, DateTime, ForeignKey)
from sqlalchemy.orm import relationship
from db import Base
from datetime import datetime


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, autoincrement=True, primary_key= True)
    name = Column(String, nullable= False)
    surname = Column(String, nullable=True)
    username = Column(String, nullable=False, unique=True)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable= False)
    birthday = Column(String, nullable= True)
    city = Column(String, nullable= True)
    reg_date = Column(DateTime, default=datetime.now())


class UserPost(Base):
    __tablename__ = "userposts"

    id = Column(Integer, autoincrement= True, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id") )
    main_text = Column(String, nullable=True)
    reg_date = Column(DateTime, default=datetime.now())

    user_fk = relationship(User, lazy="subquery")


class PostPhoto(Base):
    __tablename__ = "photos"

    id = Column(Integer, autoincrement= True, primary_key=True)
    photo_path = Column(String, nullable= False)
    post_id = Column(Integer, ForeignKey("userposts.id"), nullable=False)
    reg_date = Column(DateTime, default=datetime.now())

    post_fk = relationship(UserPost, lazy="subquery")


class Comment(Base):
    __tablename__ = "comments"
    id = Column(Integer, autoincrement= True, primary_key=True)
    text = Column(String, nullable=False)
    post_id = Column(Integer, ForeignKey('userposts.id'), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False )
    reg_date = Column(DateTime, default=datetime.now())

    user_fk = relationship(User, lazy="subquery")
    post_fk = relationship(UserPost, lazy="subquery")