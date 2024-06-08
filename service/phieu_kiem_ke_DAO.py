
from database import create_connection
from model.cart import Cart
from service.cart_product_item_DAO import list_cart_product_item_by_cart_id

# def all_cart():
#     conn = create_connection()
#     with conn.cursor() as cursor:
#         sql = "SELECT * FROM cart"
#         cursor.execute(sql)
#         results = cursor.fetchall()
#         list_cart = []
#         return list_cart