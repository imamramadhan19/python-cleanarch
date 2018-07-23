import configparser
config = configparser.ConfigParser()
config.read('config.ini')

class Config:
    
    # SQL DATABASE CONFIG
    SQL_PROVIDER=config['DATABASE_SQL']['PROVIDER']
    SQL_HOST=config['DATABASE_SQL']['HOST']
    SQL_DATABASE=config['DATABASE_SQL']['DATABASE']
    SQL_USERNAME=config['DATABASE_SQL']['USERNAME']
    SQL_PASSWORD=config['DATABASE_SQL']['PASSWORD']
    SQL_PORT=config['DATABASE_SQL']['PORT']
