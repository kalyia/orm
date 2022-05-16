
from peewee import PostgresqlDatabase, Model

db = PostgresqlDatabase('snake_film', user='kalyia', password='1234', host='localhost', port='5432')


class BaseModel(Model):

    class Meta:
        database = db