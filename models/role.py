from database.connection import Conexion

conn = Conexion()
Model = conn.model()


class Role(Model):
    __table__ = 'role'
    __primary_key__ = 'id'
    __timestamps__ = True
    __connection__ = 'postgres'

    __guarded__ = ['id']

    __fillable__ = ['name']

    __casts__ = {
        'name': 'str'
    }
