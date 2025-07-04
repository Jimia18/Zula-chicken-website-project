from app.extensions import db
from datetime import datetime

class Delivery(db.Model):
    __tablename__ = "deliveries"

    deliveryId = db.Column(db.Integer, primary_key=True, nullable=False)
    orderId = db.Column(db.Integer, db.ForeignKey("orders.orderId"), nullable=False)
    deliveryAddress = db.Column(db.String(255), nullable=False) # Ensure correct table name 
    deliveryStatus = db.Column(db.String(50), nullable=False, default="Pending")
    deliveryDate = db.Column(db.DateTime, default=datetime.now())   
    rider_name = db.Column(db.String(100), nullable=True)  
    rider_phone = db.Column(db.String(15), nullable=True)  
    rider_location = db.Column(db.String(255), nullable=True)  
    created_at = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(db.DateTime, onupdate=datetime.now())


    def __init__(self, orderId, deliveryAddress, deliveryStatus="Pending,delivered"):
        self.orderId = orderId
        self.deliveryAddress = deliveryAddress
        self.deliveryStatus = deliveryStatus

    def __repr__(self):
        return f'{self.deliveryId} {self.orderId} {self.deliveryAddress} {self.deliveryStatus}'