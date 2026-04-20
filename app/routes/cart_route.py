from flask import Blueprint, request, jsonify, render_template
from app.services.cart_service import add_item, del_item, get_cart, calculate_total,update_item
cart_bp = Blueprint('cart', __name__)
# UI Routes
@cart_bp.route('/')
def home():
    return render_template('home.html')
@cart_bp.route('/add')
def add_page():
    return render_template('add.html')

@cart_bp.route('/cart-page')
def cart_page():
    return render_template('cart.html')

@cart_bp.route('/total-page')
def total_page():
    return render_template('total.html')
# API Routes
@cart_bp.route('/cart/add', methods=['POST'])
def add():
    data = request.json
    add_item(data)
    return jsonify({"message": "Item added"}), 201
@cart_bp.route('/cart/remove/<int:id>', methods=['DELETE'])
def delete(id):
    del_item(id)
    return jsonify({"message": "Item Deleted"})
@cart_bp.route('/cart', methods=['GET'])
def view_cart():
    items = get_cart()
    return jsonify(items)
@cart_bp.route('/cart/total', methods=['GET'])
def total():
    total_price = calculate_total()
    return jsonify({"total": float(total_price)})
@cart_bp.route('/cart/update/<int:id>', methods=['PUT'])
def update(id):
    try:
        data = request.json
        update_item(id, data)
        return jsonify({"message": "Item updated"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500