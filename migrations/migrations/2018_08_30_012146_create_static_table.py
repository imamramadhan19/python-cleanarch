from orator.migrations import Migration
from config.config import Config


class CreateStaticTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('static') as table:
            table.big_increments('id')
            table.enum('contentType', ['STATIC', 'BLOCK', 'SLOT'])
            table.string('title', 70)
            table.string('subTitle', 70).nullable()
            table.string('metaTitle', 70).nullable()
            table.string('metaDescription', 320).nullable()
            table.string('placement', 50)
            table.text('content')
            table.integer('version')
            table.string('slug', 75).nullable()
            table.string('zoneId', 255).nullable()
            table.boolean('isActive')

            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('static')
