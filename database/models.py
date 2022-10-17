
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean, Date, Time, LargeBinary
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


# Used to test, will be removed later
class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    favorites = relationship('Favorite', backref='user', lazy='subquery')


# Used to test, will be removed later
class Favorite(Base):
    __tablename__ = 'favorite'
    id = Column(Integer, primary_key=True, autoincrement=True)
    symbol = Column(String)
    user_id = Column(Integer, ForeignKey('user.id'))


class Member(Base):
    __tablename__ = 'member'

    member_id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String)
    last_name = Column(String)
    cpf = Column(String)
    email = Column(String)
    password = Column(String)
    zip = Column(String)
    birthday = Column(DateTime)
    street = Column(String)
    number = Column(String)
    district = Column(String)
    city = Column(String)
    state = Column(String)
    country = Column(String)
    has_children = Column(Boolean)
    children_qty = Column(Integer)
    children_names = Column(String)
    marital_state = Column(String)
    created_at = Column(DateTime)
    status = Column(String)
    events = relationship('Events', backref='user')


class Events(Base):
    __tablename__ = 'events'

    event_id = Column(Integer, primary_key=True, autoincrement=True)
    member_id = Column(Integer, ForeignKey('member.member_id'))
    type = Column(String)
    date = Column(Date)
    start_time = Column(Time)
    end_time = Column(Time)
    warned_peers = Column(Boolean)
    warned_team = Column(Boolean)
    warned_leader = Column(Boolean)
    defined_substitute = Column(Boolean)
    substitute = Column(String)
    pending_task = Column(Boolean)
    document = Column(LargeBinary)
    created_at = Column(DateTime)
    status = Column(String)
