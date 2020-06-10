from database.connection import Conexion
from bcrypt import checkpw
from orator.orm import has_one
from models.role import Role

conn = Conexion()
Model = conn.model()


class User(Model):
    __table__ = 'user'
    __primary_key__ = 'id'
    __timestamps__ = True
    __connection__ = 'postgres'

    __guarded__ = ['id']

    __fillable__ = [
        'username', 'password', 'full_name', 'document_number', 'role_id'
    ]

    __casts__ = {
        'username': 'str',
        'password': 'str',
        'full_name': 'str',
        'document_number': 'str',
        'role_id': 'int'
    }

    __hidden__ = ['password']

    @has_one('id', 'role_id')
    def role(self):
        return Role

    def password_valid(self, password):
        return checkpw(password.encode('utf-8'), self.password.encode('utf-8'))
