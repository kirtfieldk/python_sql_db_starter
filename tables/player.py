from sqlalchemy import String, Integer, Column
from middleware import base
class Player(base):
    __tablename__='player'
    def __init__(self, id, first, last, hp):
        self.id = id
        self.first = first
        self.last = last
        self.hp = hp
    id = Column(Integer, primary_key=True)
    first = Column(String(250))
    last = Column(String(250))
    hp = Column(Integer, nullable=False)