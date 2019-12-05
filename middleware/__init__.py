from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, MetaData

metadata = MetaData()
engine = create_engine("sqlite:///teams.db")
base = declarative_base()