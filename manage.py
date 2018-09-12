from sanic.exceptions import ServerError, InvalidUsage
from src.app import create_app, connect_db
from schemas.json.loader import JSONSchemaLoader

from config.config import Config
from src.shared import response_object
from sanic.response import json

app = create_app(config=Config)

@app.listener('before_server_start')
def setup_schemas(app, loop):
    # load all json schema
    JSONSchemaLoader.load(path='schemas/json/', filename="*.json")

@app.listener('before_server_start')
def setup_db(app, loop):
    app.db = connect_db()


@app.listener('after_server_stop')
def close_db(app, loop):
    app.db.disconnect()


@app.exception(InvalidUsage)
def invalid_usage(request, exception):
    if Config.DEBUG: return exception
    response = response_object.ResponseFailure.build_system_error(
        "{}: {}".format(exception.__class__.__name__, "{}".format(exception))
    )
    return json(response.value, status=Config.STATUS_CODES[response.type])

if __name__ == '__main__':
    app.run(host=Config.HOST, port=int(Config.PORT), debug=Config.DEBUG)
