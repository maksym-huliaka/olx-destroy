import psycopg2

from modules.util.config import config



def connect():
    host        = config().get('db.host')
    database    = config().get('db.database')
    user        = config().get('db.user')
    password    = config().get('db.password')
    port        = config().get('db.port')
    connection = None
    try:
        connection = psycopg2.connect(
            host = host,
            database = database,
            user = user,
            password = password)
        return connection
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

