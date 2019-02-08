from connections import connection

# config have credential data to connect into database
import config


class Product:
    def get_a_product(self, data):
        if not data["id"]:
            return {"error": "ID should not empty"}

        if isinstance(data["id"], str):
            return {"error": TypeError}

        if isinstance(data["id"], list):
            return {"error": "ID should not list type"}

        product = self.query_by_id(data["id"])

        if not product:
            return {"error": "ID should not empty"}
        return product

    def query_by_id(self, id):
        sql = self.query_db(f"SELECT id, product_name FROM product WHERE id={id}")
        return sql

    def query_db(self, query):
        try:
            conn = connection(config.credential)
            cur = conn.cursor()
            cur.execute(query)
            r = [
                dict((cur.description[i][0], value) for i, value in enumerate(row))
                for row in cur.fetchall()
            ]
            cur.close()
            return r
        except Exception as e:
            return e
        finally:
            if conn is not None:
                conn.close()
