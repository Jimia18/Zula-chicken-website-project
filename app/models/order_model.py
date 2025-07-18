from app.extensions import db  # Import db after it's initialized in __init__.py
from datetime import datetime

class Order(db.Model):
    __tablename__ = "orders"
    orderId = db.Column(db.Integer,primary_key = True, nullable=False)
    order_date = db.Column(db.String(150),nullable = False)
    total_amount = db.Column(db.String(22), nullable=False, default="UGX")
    status = db.Column(db.Text(),nullable = False)
    userId = db.Column(db.Integer, db.ForeignKey("users.userId"))  # Ensure correct table name
    customerId = db.Column(db.Integer, db.ForeignKey("customers.customerId"))  # Ensure correct table name

    user = db.relationship("User", backref="orders")
    customer = db.relationship("Customer", backref="orders")
    order_items = db.relationship("OrderItem", backref="order", lazy=True)


    created_at = db.Column(db.DateTime,default=datetime.now())
    updated_at = db.Column(db.DateTime,onupdate=datetime.now())

def __init__(self,order_date,status,total_amount = 'UGX'):
        super(Order, self).__init__()
        self.order_date = order_date
        self.total_amount = total_amount
        self.status = status
          

def __repr__(self):
      return f'{self.order_date} {self.total_amount}{self.status}'