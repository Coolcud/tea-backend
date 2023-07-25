from app import db
from sqlalchemy import ARRAY

class Boba_Order(db.Model):
    # Columns
    order_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    base = db.Column(db.String)
    toppings = db.Column(ARRAY(db.String))
    temp = db.Column(db.String)
    sweetness = db.Column(db.String)

    def to_dict(self):
        return {
            "order_id": self.order_id,
            "base": self.base,
            "toppings": self.toppings,
            "temp": self.temp,
            "sweetness": self.sweetness
        }
    
    @classmethod
    def from_dict(cls, order_data):
        return cls(
            base=order_data["base"],
            toppings=order_data["toppings"],
            temp=order_data["temp"],
            sweetness=order_data["sweetness"]
        )