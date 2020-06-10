from database.connection import Conexion

conn = Conexion()
Model = conn.model()


class Product(Model):
    __table__ = 'role'
    __primary_key__ = 'id'
    __timestamps__ = True
    __connection__ = 'postgres'

    __guarded__ = ['id']

    __fillable__ = ['name', 'stock', 'cost_per_unit']

    __casts__ = {
        'name': 'str',
        'stock': 'float',
        'cost_per_unit': 'str'
    }
