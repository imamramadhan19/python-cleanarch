import redis
from orator import DatabaseManager
from sanic import Sanic

from config.config import Config
from src.articles.delivery.http_sanic import bp_articles


def connect_db():
    # postgres use pgsql
    config = {
        'postgres': {
            'driver': Config.DB_TYPE, 
            'host': Config.DB_HOST,
            'database': Config.DB_NAME,
            'user': Config.DB_USER,
            'password': Config.DB_PASS,
            'prefix': '',
            'log_queries': True,
        }
    }
    return DatabaseManager(config)


def create_app(config):
    app = Sanic(__name__)
    app.config.from_object(config)
    app.blueprint(bp_articles)

    return app