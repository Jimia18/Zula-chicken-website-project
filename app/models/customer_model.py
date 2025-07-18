from app.extensions import db
from datetime import datetime

class Customer(db.Model):
    __tablename__ = "customers"
    customerId = db.Column(db.Integer, primary_key=True, nullable=False)
    customer_name = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(150), nullable=False, unique=True)
    phone_number = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.Text(), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(db.DateTime, onupdate=datetime.now())

    def __init__(self, customer_name, email, phone_number, password):
        super(Customer, self).__init__()
        self.customer_name = customer_name
        self.email = email
        self.phone_number = phone_number
        self.password = password

    def __repr__(self):
        return {self.customer_name}
