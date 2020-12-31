from sqlalchemy.sql import Select

from app.loader import db
from app.models import UserRelatedModel
from app.models.base import TimedBaseModel


class Mealtime(TimedBaseModel):
    __tablename__ = 'mealtimes'
    id = db.Column(db.BigInteger, primary_key=True, index=True, unique=True)
    user_id = UserRelatedModel.user_id
    query: Select
