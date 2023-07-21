from app import db
from sqlalchemy import ARRAY

class Order(db.Model):
    # Columns
    order_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    base = db.Column(db.String)
    toppings = db.Column(ARRAY(db.String))
    temp = db.Column(db.String)
    sweetness = db.Column(db.Integer)