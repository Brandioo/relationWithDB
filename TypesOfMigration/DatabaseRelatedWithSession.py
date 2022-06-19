from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from TypesOfMigration.MigrateSQL import Directors, Movies

eng = create_engine('mysql+mysqlconnector://root:Gonlinepro892!@localhost:3306/cinematic_alchemy')
# drop_database(eng.url)
# if not database_exists(eng.url):
#     create_database(eng.url)


with Session(eng) as session:
    spongebob = Directors(
        name="Spongebob",
        surname="Squarepants",
        rating=5,
        movies=[Movies(title="Sponge Bob Square Pants", year=2022, rating=5)]
    )
    sandy = Directors(
        name="Sandy",
        surname="Cheeks",
        rating=5,
        movies=[
            Movies(title="Sandy Cheeks", year=2022, rating=5),
            Movies(title="Sandy Cheeks", year=2022, rating=5),
        ],
    )
    patrick = Directors(
        name="Patrick",
        surname="Star",
        rating=5,
        movies=[Movies(title="Patrick", year=2022, rating=5)])

    session.add_all([spongebob, sandy, patrick])

    session.commit()
