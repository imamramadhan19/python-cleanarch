from orator import DatabaseManager
from sanic import Sanic

from config import Config
from src.posts.delivery.http.index import bp_posts


def create_app(config_object=Config):

    app = Sanic(__name__)
    app.config.from_object(config_object)
    app.blueprint(bp_posts)

    return app


def connect_db():

    config = {
        'postgresql': {
            'driver': 'pgsql',
            'host': Config.SQL_HOST,
            'database': Config.SQL_DATABASE,
            'user': Config.SQL_USERNAME,
            'password': Config.SQL_PASSWORD,
            'prefix': '',
            'port':Config.SQL_PORT
        }
    }

    return DatabaseManager(config)
