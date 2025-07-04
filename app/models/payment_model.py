from app.extensions import db
from datetime import datetime

class Payment(db.Model):
    __tablename__ = "payments"

    paymentId = db.Column(db.Integer, primary_key=True, nullable=False)
    orderId = db.Column(db.Integer, db.ForeignKey("orders.orderId"), nullable=False)
    paymentMethod = db.Column(db.String(50), nullable=False)
    paymentStatus = db.Column(db.String(50), nullable=False, default="Pending,paid")
    paymentDate = db.Column(db.DateTime, default=datetime.now())
    amount = db.Column(db.String(10), nullable=False,default='UGX')

    def __init__(self, orderId, paymentMethod, paymentStatus="Pending,paid", amount='UGX'):
        self.orderId = orderId
        self.paymentMethod = paymentMethod
        self.paymentStatus = paymentStatus
        self.amount = amount

    def __repr__(self):
        return f'{self.paymentId} {self.orderId} {self.paymentMethod} {self.paymentStatus} {self.amount}'