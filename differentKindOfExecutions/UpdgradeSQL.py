import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

eng = sqlalchemy.create_engine('mysql+mysqlconnector://root:Gonlinepro892!@localhost:3306/cinematic')
print(eng)
print(sqlalchemy.__version__)