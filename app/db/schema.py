from uuid import uuid4
from enum import Enum
from sqlalchemy.dialects.postgresql import UUID, ENUM
from sqlalchemy import Table, Column, Integer, String, MetaData
from sqlalchemy.sql.schema import ForeignKey


class OrderState(Enum):
    RECEIVED = 1
    TAKEN = 2
    DELIVERED = 3

convention = {
    'all_column_names': lambda constraint, table: '_'.join([
        column.name for column in constraint.columns.values()
    ]),
    'ix': 'ix__%(table_name)s__%(all_column_names)s',
    'uq': 'uq__%(table_name)s__%(all_column_names)s',
    'ck': 'ck__%(table_name)s__%(constraint_name)s',
    'fk': 'fk__%(table_name)s__%(all_column_names)s__%(referred_table_name)s',
    'pk': 'pk__%(table_name)s'
}

meta = MetaData(naming_convention=convention)

restaurants = Table(
    'Restaurants', meta,
    Column('id', Integer, primary_key=True),
    Column('external_id', UUID(as_uuid=False), default=uuid4),
    Column('coords', String(60), nullable=False),
    Column('name', String(60), nullable=False)
)

orders = Table(
    'Orders', meta,
    Column('id', Integer, primary_key=True),
    Column('external_id', UUID(as_uuid=False), default=uuid4),
    Column('content', String(60), nullable=False),
    Column('comment', String(60), nullable=False),
    Column('state', ENUM(OrderState), nullable=False),
    Column('restaurant_id', Integer, ForeignKey('Restaurants.id'), nullable=False)
)

dishes = Table(
    'Dishes', meta,
    Column('id', Integer, primary_key=True),
    Column('external_id', UUID(as_uuid=False), default=uuid4),
    Column('price', Integer, default=0, nullable=False),
    Column('restaurant_id', Integer, ForeignKey('Restaurants.id'))
)

orders_to_dishes = Table(
    'OrdersToDishes', meta,
    Column('id', Integer, primary_key=True),
    Column('amount', Integer, default=1, nullable=False),
    Column('dish_id', Integer, ForeignKey('Dishes.id')),
    Column('order_id', Integer, ForeignKey('Orders.id'))
)
