from app.extensions import db  # Import db after it's initialized in __init__.py
from datetime import datetime

class CartModel(db.Model): 
    __tablename__ = "carts"

    cartId = db.Column(db.Integer, primary_key=True, nullable=False)
    customerId = db.Column(db.Integer, db.ForeignKey("customers.customerId"), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(db.DateTime, onupdate=datetime.now())

    def __init__(self, customerId):
        self.customerId = customerId

    def __repr__(self):
        return f'{self.cartId} {self.customerId}'