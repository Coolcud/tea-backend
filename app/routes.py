from flask import Blueprint, request, jsonify, make_response, abort
from app import db
from app.models.order import Order
from dotenv import load_dotenv
import os


orders_bp = Blueprint("orders_bp", __name__, url_prefix="/orders")

def validate_model_item(model, item_id):
    """Validate model item exists in database."""
    try:
        item_id = int(item_id)
    except:
        abort(make_response({"message": f"ID '{item_id}' invalid"}, 400))

    item = model.query.get(item_id)
    if not item:
        abort(make_response({"message": f"ID '{item_id}' not found"}, 404))

    return item


# --------------------------ORDER ROUTES--------------------------

@orders_bp("", methods=["GET"])
def get_all_orders():
    """Retrieve all orders from database."""
    all_orders = Order.query.all()

    response = [order.to_dict() for order in all_orders]

    return jsonify(response), 200


@orders_bp("", methods=["POST"])
def create_order():
    """Add new order to database"""
    request_body = request.get_json()

    new_order = Order.from_dict(request_body)

    db.session.add(new_order)
    db.session.commit()

    return {"order": new_order.to_dict()}, 201
