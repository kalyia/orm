from peewee import (CharField, IntegerField)

from db import base


class FilmModel(base.BaseModel):

    order = IntegerField()
    value = CharField(max_length=50)
    title = CharField(max_length=50)

    