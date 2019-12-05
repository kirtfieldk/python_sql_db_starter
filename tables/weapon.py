from sqlalchemy import String, Integer, Column
from middleware import base

class Weapon(base):
    __tablename__="weapon"
    
    def __init__(self, name, powerlevel, player_id, id):
        self.id = id
        self.name = name
        self.powerlevel = powerlevel
        self.player_id = player_id

    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    powerlevel = Column(Integer)
    player_id = Column(Integer)


