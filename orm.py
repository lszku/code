from sqlalchemy import Column, ForeignKey, Integer, String, BigInteger, MetaData, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, mapper

import model

metadata = MetaData()

order_lines = Table(
    'order_lines', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('sku', String(255)),
    Column('qty'),
    Column('orderid', String(255)),
)


def start_mappers():
    order_lines_mapper = mapper(model.OrderLine, order_lines)
