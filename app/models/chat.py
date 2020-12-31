from app.loader import db
from app.models.base import BaseModel, TimedBaseModel


class Chat(TimedBaseModel):
    __tablename__ = "chats"

    id = db.Column(db.BigInteger, primary_key=True, index=True)
    type = db.Column(db.String)


class ChatRelatedModel(BaseModel):
    __abstract__ = True

    chat_id = db.Column(
        db.ForeignKey(f"{Chat.__tablename__}.id", ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False,
    )