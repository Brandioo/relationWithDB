from sqlalchemy import create_engine, select
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, Date, ForeignKey
from sqlalchemy_utils import database_exists, create_database, drop_database
from sqlalchemy.orm import sessionmaker, relationship

eng = create_engine('mysql+mysqlconnector://root:Gonlinepro892!@localhost:3306/cinematic_alchemy')

drop_database(eng.url)
if not database_exists(eng.url):
    create_database(eng.url)

print(database_exists(eng.url))

base = declarative_base()


class Directors(base):
    __tablename__ = "directors"

    director_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    surname = Column(String(50), nullable=False)
    rating = Column(Integer, nullable=False)

    movies = relationship(
        "Movies", back_populates="directors", cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"Directors(director_id={self.director_id!r}, name={self.name!r}, surname={self.surname!r}, rating={self.rating!r})"


class Movies(base):
    __tablename__ = "movies"

    movie_id = Column(Integer, primary_key=True, autoincrement=True)
    # email_address = Column(String, nullable=False)
    title = Column(String(255), nullable=False)
    year = Column(Integer, nullable=False)
    director_id = Column(Integer, ForeignKey("directors.director_id"), nullable=False)
    rating = Column(Integer, nullable=False)

    directors = relationship("Directors", back_populates="movies")

    def __repr__(self):
        return f'<Movies: id={self.movie_id}, title={self.title}, year={self.year}, category={self.category}, director_id={self.director_id}, rating={self.rating}>'

base.metadata.create_all(eng)
