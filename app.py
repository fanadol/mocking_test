import product
import connections


def connect(credential):
    return connections.connection(credential)


def query_product_id(id):
    p = product.Product()
    x = p.get_a_product(id)
    return x
