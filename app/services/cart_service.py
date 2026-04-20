from app.db import mysql
def add_item(data):
    try:
        cur = mysql.connection.cursor()
        cur.execute(
            "INSERT INTO cart_items (product_name, price, quantity) VALUES (%s, %s, %s)",
            (data['product_name'], data['price'], data['quantity'])
        )
        mysql.connection.commit()
    except Exception as e:
        mysql.connection.rollback()
        raise Exception(f"Error adding item: {str(e)}")
    finally:
        cur.close()
def del_item(item_id):
    try:
        cur = mysql.connection.cursor()
        cur.execute("DELETE FROM cart_items WHERE id=%s", (item_id,))
        if cur.rowcount == 0:
            raise Exception("Item not found")
        mysql.connection.commit()
    except Exception as e:
        mysql.connection.rollback()
        raise Exception(f"Error deleting item: {str(e)}")
    finally:
        cur.close()
def get_cart():
    try:
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM cart_items")
        rows = cur.fetchall()
        result = []
        for row in rows:
            result.append({
                "id": row[0],
                "product_name": row[1],
                "price": row[2],
                "quantity": row[3]
            })
        return result
    except Exception as e:
        raise Exception(f"Error fetching cart: {str(e)}")
    finally:
        cur.close()
def calculate_total():
    try:
        cur = mysql.connection.cursor()
        cur.execute("SELECT SUM(price * quantity) FROM cart_items")
        result = cur.fetchone()
        total_price = result[0] if result[0] is not None else 0
        return total_price
    except Exception as e:
        raise Exception(f"Error calculating total: {str(e)}")
    finally:
        cur.close()
def update_item(item_id, data):
    try:
        cur = mysql.connection.cursor()
        cur.execute(
            "UPDATE cart_items SET product_name=%s, price=%s, quantity=%s WHERE id=%s",
            (data['product_name'], data['price'], data['quantity'], item_id)
        )
        if cur.rowcount == 0:
            raise Exception("Item not found")
        mysql.connection.commit()
    except Exception as e:
        mysql.connection.rollback()
        raise Exception(f"Error updating item: {str(e)}")
    finally:
        cur.close()