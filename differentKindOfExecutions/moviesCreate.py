from sqlalchemy import create_engine, select, desc, asc, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, Date, ForeignKey
from sqlalchemy_utils import database_exists, create_database, drop_database
from sqlalchemy.orm import sessionmaker, relationship

eng = create_engine('mysql+mysqlconnector://root:Gonlinepro892!@localhost:3306/cinematic')

print(database_exists(eng.url))

base = declarative_base()


class Directors(base):
    __tablename__ = 'directors'

    director_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    surname = Column(String(255), nullable=False)
    rating = Column(Integer, nullable=False)

    movies = relationship("Movies", back_populates="directors", cascade="all, delete-orphan")

    def __repr__(self):
        return f'<Directors: id={self.director_id}, name={self.name}, surname={self.surname}, rating={self.rating}>'


class Movies(base):
    __tablename__ = 'movies'

    movie_id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(255), nullable=False)
    year = Column(Integer, nullable=False)
    category = Column(String(255), nullable=False)
    director_id = Column(Integer, ForeignKey("directors.director_id"), nullable=False)
    rating = Column(Integer, nullable=False)

    directors = relationship("Directors", back_populates="movies")

    def __repr__(self):
        return f'<Movies: id={self.movie_id}, title={self.title}, year={self.year}, category={self.category}, director_id={self.director_id}, rating={self.rating}>'


base.metadata.create_all(eng)

Session = sessionmaker(bind=eng)
session = Session()
stmt = select([Movies.category,(Movies.rating),Movies.year]).\
    where(Movies.year.between(2000,2010)).order_by((desc(Movies.rating)))
result = eng.execute(stmt).fetchall()
print(result)
for record in result:
    if record[1] > 7:
        print(record[0],record[1])


result = session.query(Movies.category,(Movies.rating)).\
    filter(Movies.year.between(2000,2010)).order_by((desc(Movies.rating))).all()
for record in result:
    if record[1] > 7:
        print(record[0],record[1])
