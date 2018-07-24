from src.app import create_app, connect_db

app = create_app()

@app.listener('before_server_start')
def setup_db(app, loop):
    app.db = connect_db()


@app.listener('after_server_stop')
def close_db(app, loop):
    app.db.disconnect()


if __name__ == '__main__':
    app.run()