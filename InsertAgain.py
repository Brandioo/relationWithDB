import MySQLdb

db = MySQLdb.connect(host="localhost", user="root", passwd="SDA19912022!", database="music")


def insert_instruments(connection, instrument_values):
    if not instrument_values:
        return
    insert_sql = """INSERT INTO instruments (name, family, difficulty) VALUES(%s, %s, %s)"""
    connection.cursor().executemany(insert_sql, instrument_values)
    connection.commit()


instruments = [
    ('guitar', 'strings', 'medium'),
    ('piano', 'keyboard', 'hard'),
    ('harp', 'strings', 'hard'),
    ('triangle', 'percussion', 'easy'),
    ('flute', 'woodwind', 'medium'),
    ('violin', 'string', 'medium'),
    ('tambourine', 'percussion', 'easy'),
    ('organ', 'keyboard', 'hard')]
with db:
    insert_instruments(db, instruments)