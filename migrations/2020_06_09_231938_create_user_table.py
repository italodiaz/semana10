from orator.migrations import Migration


class CreateUserTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('user') as table:
            table.increments('id')
            table.string('username')
            table.string('password')
            table.string('full_name')
            table.string('document_number')
            table.integer('role_id')
            table.foreign('role_id').references('id').on('role')
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('user')
