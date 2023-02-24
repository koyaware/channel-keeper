from gino import Gino
from sqlalchemy import Column, String, ForeignKey, BigInteger

db = Gino()


class Users(db.Model):

    __tablename__ = "users"

    tg_id = Column(BigInteger(), primary_key=True)


class Channels(db.Model):

    __tablename__ = "channels"

    Id = Column(BigInteger(), primary_key=True)
    name = Column(String(120))
    link = Column(String(120))
    user_id = Column(ForeignKey("users.tg_id"))