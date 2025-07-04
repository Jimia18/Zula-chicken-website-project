from app.extensions import db  # Import db after it's initialized in __init__.py
from datetime import datetime       

class CartItem(db.Model):
    __tablename__ = "cartItems"

    cartItemId = db.Column(db.Integer, primary_key=True, nullable=False)
    customerId = db.Column(db.Integer, db.ForeignKey("customers.customerId"), nullable=False)
    menuItemId = db.Column(db.Integer, db.ForeignKey("menuItems.menuItemId"), nullable=False)
    quantity = db.Column(db.Integer, nullable=False, default=1)
    created_at = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(db.DateTime, onupdate=datetime.now())

    def __init__(self, customerId, menuItemId, quantity):
        self.customerId = customerId
        self.menuItemId = menuItemId
        self.quantity = quantity

    def __repr__(self):
        return f'{self.cartItemId} {self.customerId} {self.menuItemId} (x{self.quantity})'