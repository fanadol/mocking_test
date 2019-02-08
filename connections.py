import psycopg2


def connection(credential):
    try:
        conn = psycopg2.connect(
            host=credential['host'],
            user=["user"],
            password=["password"],
            dbname=["dbname"],
            port=credential['port'],
        )
    except Exception as e:
        raise e

    return conn
