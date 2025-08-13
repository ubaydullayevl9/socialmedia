from sqlalchemy import (Integer, Column, String, DateTime, ForeignKey)
from sqlalchemy.orm import relationship
from db import Base
from datetime import datetime, timezone


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String, nullable=False)
    surname = Column(String, nullable=True)
    username = Column(String, nullable=False, unique=True)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    birthday = Column(String, nullable=True)
    city = Column(String, nullable=True)
    reg_date = Column(DateTime, default=lambda: datetime.now(timezone.utc))

    posts = relationship("UserPost", back_populates="user", cascade="all, delete-orphan")
    comments = relationship("Comment", back_populates="user", cascade="all, delete-orphan")


class UserPost(Base):
    __tablename__ = "userposts"

    id = Column(Integer, autoincrement=True, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    main_text = Column(String, nullable=False)
    reg_date = Column(DateTime, default=lambda: datetime.now(timezone.utc))

    # Python-side relation (not a DB column)
    user = relationship("User", back_populates="posts", lazy="joined")
    photos = relationship("PostPhoto", back_populates="post", cascade="all, delete-orphan")
    comments = relationship("Comment", back_populates="post", cascade="all, delete-orphan")


class PostPhoto(Base):
    __tablename__ = "photos"
    id = Column(Integer, autoincrement=True, primary_key=True)
    photo_path = Column(String, nullable=False)
    post_id = Column(Integer, ForeignKey("userposts.id", ondelete="CASCADE"), nullable=False)
    reg_date = Column(DateTime, default=lambda: datetime.now(timezone.utc))

    post = relationship("UserPost", back_populates="photos", lazy="joined")


class Comment(Base):
    __tablename__ = "comments"
    id = Column(Integer, autoincrement=True, primary_key=True)
    text = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    post_id = Column(Integer, ForeignKey("userposts.id", ondelete="CASCADE"), nullable=False)
    reg_date = Column(DateTime, default=lambda: datetime.now(timezone.utc))

    user = relationship("User", back_populates="comments", lazy="joined")
    post = relationship("UserPost", back_populates="comments", lazy="joined")