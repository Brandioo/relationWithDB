from sqlalchemy import create_engine, select
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, Date, ForeignKey
from sqlalchemy_utils import database_exists, create_database, drop_database
from sqlalchemy.orm import sessionmaker, relationship

eng = create_engine('mysql+mysqlconnector://root:GonlinePro892!@localhost:3306/cinematic_alchemy')
drop_database(eng.url)
if not database_exists(eng.url):
    create_database(eng.url)

print(database_exists(eng.url))