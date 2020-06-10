from orator.seeds import Seeder
from bcrypt import hashpw, gensalt


class DatabaseSeeder(Seeder):

    def run(self):
        """
        Run the database seeds.
        """
        self.db.statement('TRUNCATE TABLE role RESTART IDENTITY CASCADE;')
        admin_id = self.db.table('role').insert_get_id(
            {'name': 'administrator'}
        )
        self.db.table('role').insert([
            {'name': 'cashier'},
            {'name': 'storekeeper'}
        ])
        password = hashpw('12345'.encode('utf-8'), gensalt())
        self.db.table('user').insert({
            'username': 'admin',
            'password': password.decode('utf-8'),
            'full_name': 'Italo Diaz',
            'document_number': '12345678',
            'role_id': admin_id
        })
