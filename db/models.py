from db import  (films, base)


def create_table():
    print('Connect database')
    base.db.connect()
    base.db.create_tables([films.FilmModel])


