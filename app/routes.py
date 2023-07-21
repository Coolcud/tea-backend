from flask import Blueprint, request, jsonify, make_response, abort
from app import db
from app.models.boba_order import Boba_Order
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

@orders_bp.route("", methods=["GET"])
def get_all_orders():
    """Retrieve all orders from database."""
    all_orders = Boba_Order.query.all()

    response = [order.to_dict() for order in all_orders]

    return jsonify(response), 200


@orders_bp.route("", methods=["POST"])
def create_order():
    """Add new order to database."""
    request_body = request.get_json()

    new_order = Boba_Order.from_dict(request_body)

    db.session.add(new_order)
    db.session.commit()

    return {"order": new_order.to_dict()}, 201


@orders_bp.route("/<order_id>", methods=["DELETE"])
def delete_order(order_id):
    """Delete order via order_id."""
    order = validate_model_item(Boba_Order, order_id)

    db.session.delete(order)
    db.session.commit()

    return jsonify({"message": f"Order #{order_id} has been successfully deleted!"}), 200
