from app.extensions import  db
from datetime import datetime

class ContactMessage(db.Model):
    __tablename__ = "contactMessages"

    messageId = db.Column(db.Integer, primary_key=True, nullable=False)
    customerId = db.Column(db.Integer, db.ForeignKey("customers.customerId"), nullable=False)
    subject = db.Column(db.String(255), nullable=False)
    message = db.Column(db.Text(), nullable=False)
    submitted_at = db.Column(db.DateTime, default=datetime.now())   
    created_at = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(db.DateTime, onupdate=datetime.now())

    def __init__(self, customerId, subject, message):
        self.customerId = customerId
        self.subject = subject
        self.message = message

    def __repr__(self):
        return f'{self.messageId} {self.customerId} {self.subject}'