import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine


# Used to create a base class that our class code will inherit
Base = declarative_base()


# Database mapper code for User table (authenticated users).
class User(Base):
# Create Users table
    __tablename__= 'user'
# Map User table columns
    userID = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    picture = Column(String(250))


# Database mapper code for Sports table
class Competition(Base):
# Create Sports table
    __tablename__= 'sports'
# Map Sports table columns
    sportID = Column(Integer, primary_key=True)
    sport = Column(String(80), nullable=False)
    user_id = Column(Integer, ForeignKey('user.userID'))
    user = relationship(User)

# JSON sport data conversion to serializeable format
    @property
    def serialize(self):
        return {
            'sportID': self.sportID,
            'sport': self.sport,
        }


# Database mapper code for Players table.
class Athlete(Base):
# Create Players table
    __tablename__= 'players'
# Map Players table columns
    playerID = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    position = Column(String(250))
    team = Column(String(250))
    career_stats = Column(String(250))
    sport_id = Column(Integer, ForeignKey('sports.sportID'))
    sport = relationship(Competition)
    user_id = Column(Integer, ForeignKey('user.userID'))
    user = relationship(User)

# JSON player data conversion to serializeable format.
    @property
    def serialize(self):
        return {
            'playerID': self.playerID,
            'name': self.name,
            'position': self.position,
            'team': self.team,
            'career_stats': self.career_stats,
        }


# insert at end of file #
engine = create_engine('sqlite:///sportscatalog.db')

Base.metadata.create_all(engine)
