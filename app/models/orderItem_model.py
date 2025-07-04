from app.extensions import db  # Import db after it's initialized in __init__.py
from datetime import datetime

class OrderItem(db.Model):
    __tablename__ = "orderitems"
    orderItemId = db.Column(db.Integer,primary_key = True, nullable=False)
    quantity = db.Column(db.String(150),nullable = False)
    orderId = db.Column(db.Integer, db.ForeignKey("orders.orderId"))  # Ensure correct table 
    menuItemId = db.Column(db.Integer, db.ForeignKey("menuItems.menuItemId"))
    created_at = db.Column(db.DateTime,default=datetime.now())
    updated_at = db.Column(db.DateTime,onupdate=datetime.now())

def __init__(self,orderItemId,quantity):
        super(OrderItem, self).__init__()
        self.orderItemId = orderItemId
        self.quantity = quantity

        
          

def __repr__(self):
      return f'{self.orderItemId} {self.quantity}'