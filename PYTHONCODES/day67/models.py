from extensions import db
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List
from sqlalchemy import Integer, String, Text, Boolean, ForeignKey
from flask_login import (
    UserMixin,
    login_user,
    LoginManager,
    login_required,
    current_user,
    logout_user,
)


class User(db.Model, UserMixin):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(100))
    name: Mapped[str] = mapped_column(String(1000))
    is_admin: Mapped[bool] = mapped_column(Boolean, default=False)

    posts: Mapped[List["BlogPost"]] = relationship(
        back_populates="author", cascade="all, delete-orphan"
    )

    comments: Mapped[List["Comment"]] = relationship(
        back_populates="author", cascade="all, delete-orphan"
    )


class BlogPost(db.Model):
    __tablename__ = "blog_post"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    subtitle: Mapped[str] = mapped_column(String(250), nullable=False)
    date: Mapped[str] = mapped_column(String(250), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)

    author_id: Mapped[int] = mapped_column(ForeignKey("user.id", ondelete="CASCADE"))

    author: Mapped["User"] = relationship(back_populates="posts")

    comments: Mapped[List["Comment"]] = relationship(
        back_populates="post", cascade="all, delete-orphan"
    )


class Comment(db.Model):
    __tablename__ = "comment"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    text: Mapped[str] = mapped_column(Text, nullable=False)

    user_id: Mapped[int] = mapped_column(ForeignKey("user.id", ondelete="CASCADE"))

    post_id: Mapped[int] = mapped_column(ForeignKey("blog_post.id", ondelete="CASCADE"))

    author: Mapped["User"] = relationship(back_populates="comments")
    post: Mapped["BlogPost"] = relationship(back_populates="comments")
