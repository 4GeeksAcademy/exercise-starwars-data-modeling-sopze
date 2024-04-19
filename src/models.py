import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Enum
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

"""
    user (a basic user instance)
"""
class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    password = Column(String(16), nullable=False)

"""
    group (item types, such as 'character', 'vehicle', 'film', etc...)
"""
class Group(Base):
    __tablename__ = 'group'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)

"""
    item (item instance)
    foreign keys : 
        group (the group this item belongs to)
"""
class Item(Base):
    __tablename__ = 'item'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    group_id = Column(Integer, ForeignKey('group.id')) # intentionally nullable
    group = relationship(Group)

"""
    bookmark (user saved item)
    foreign keys : 
        user (the user this item belongs to)
        item (the item this bookmark points to)
"""
class Bookmark(Base):
    __tablename__ = 'bookmark'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    item_id = Column(Integer, ForeignKey('item.id'), nullable=False)
    user = relationship(User)
    item = relationship(Item)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
