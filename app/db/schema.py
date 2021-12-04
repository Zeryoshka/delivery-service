from uuid import uuid4
from sqlalchemy.dialects.postgresql import UUID, ENUM
from sqlalchemy import Table, Column, Integer, String, MetaData
from sqlalchemy.sql.schema import ForeignKey

meta = MetaData()
states = ENUM(
    'RECEIVED',
    'TAKEN',
    'DELIVERED',
    name='states_enum'
)

restaurants = Table(
    'Restaurants', meta,
    Column(name='id', type_=Integer, primary_key=True),
    Column(name='external_id', type_=UUID(as_uuid=False), default=uuid4),
    Column(name='coords', type=String(60), nullable=False),
    Column(name='name', type=String(60), nullable=False)
)

orders = Table(
    'Orders', meta,
    Column(name='id', type_=Integer, primary_key=True),
    Column(name='external_id', type_=UUID(as_uuid=False), default=uuid4),
    Column(name='content', type=String(60), nullable=False),
    Column(name='comment', type=String(60), nullable=False),
    Column(name='state', type_=states, nullable=False),
    Column(name='restaurant_id', type=Integer, foreign_key=ForeignKey('Restaurants.id'))
)

dishes = Table(
    'Dishes', meta,
    Column(name='id', type_=Integer, primary_key=True),
    Column(name='external_id', type_=UUID(as_uuid=False), default=uuid4),
    Column(name='price', type=Integer, default=0, nullable=False),
    Column(name='restaurant_id', type=Integer, foreign_key=ForeignKey('Restaurants.id'))
)

orders_to_dishes = Table(
    'OrdersToDishes', meta,
    Column(name='id', type_=Integer, primary_key=True),
    Column(name='dish_id', type=Integer, foreign_key=ForeignKey('Dishes.id')),
    Column(name='order_id', type=Integer, foreign_key=ForeignKey('Orders.id'))
)