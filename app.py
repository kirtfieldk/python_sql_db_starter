
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from middleware import base, engine, MetaData
from tables.player import Player
from tables.weapon import Weapon


Session = sessionmaker(bind=engine)
session = Session()


base.metadata.create_all(engine)
# p1 = Player(12,"Keith", "Kirtfield", 5000)
# session.add(p1)
# w1 = Weapon("Oden", 1200, 1, 1)
# session.add(w1)
# session.commit()
res = session.query(Player).all()


for p, w in session.query(Player, Weapon).filter(Player.id == Weapon.player_id).all():
    print("name: {}, weapon: {}".format(p.first, w.name))