from app.extensions  import db
from datetime import datetime


class Review(db.Model):
    __tablename__ = "reviews"
    reviewId = db.Column(db.Integer, primary_key=True, nullable=False)
    customerId = db.Column(db.Integer, db.ForeignKey("customers.customerId"), nullable=False)
    menuItemId = db.Column(db.Integer, db.ForeignKey("menuItems.menuItemId"), nullable=False)
    vendorId = db.Column(db.Integer, db.ForeignKey("vendors.vendorId"), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.Text(), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(db.DateTime, onupdate=datetime.now())

    def __init__(self, customerId, vendorId, rating, comment=None):
        self.customerId = customerId
        self.vendorId = vendorId
        self.rating = rating
        self.comment = comment

    def __repr__(self):
        return f' {self.reviewI} {self.customerId} {self.vendorId}'