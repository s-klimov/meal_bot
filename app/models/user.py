from sqlalchemy.sql import Select, expression

from app.loader import db
from app.models.base import BaseModel, TimedBaseModel


class User(TimedBaseModel):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True, index=True, unique=True)
    email = db.Column(db.String, unique=True)
    is_superuser = db.Column(db.Boolean, server_default=expression.false())
    query: Select


class UserRelatedModel(BaseModel):
    __abstract__ = True

    user_id = db.Column(
        db.ForeignKey(f"{User.__tablename__}.id", ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False,
    )
