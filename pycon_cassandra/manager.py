import datetime

from cassandra.cqlengine import connection
from cassandra.cqlengine.management import (
    create_keyspace_simple,
    sync_table,
)
from .models import BeerometerModel


def create_keyspace_from_name(keyspace):
    connection.setup(['127.0.0.1'], 'system')

    create_keyspace_simple(keyspace, 1)

    return keyspace


def create_model(keyspace):
    connection.setup(['127.0.0.1'], keyspace)

    sync_table(BeerometerModel)


def fill_model(keyspace, brand):
    connection.setup(['127.0.0.1'], keyspace)

    beerometer = BeerometerModel.create(
        brand=brand,
        created_at=datetime.datetime.now()
    )

    return beerometer.to_dict()
