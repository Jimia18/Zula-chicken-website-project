from app.extensions import db  # Import db after it's initialized in __init__.py
from datetime import datetime

class Feedback(db.Model):
    __tablename__ = "feedbacks"
    feedbackId = db.Column(db.Integer,primary_key = True, nullable=False)
    message = db.Column(db.String(150),nullable = False)
    rating= db.Column(db.Integer,nullable = False)
    feedback_date = db.Column(db.Date,nullable = False)
    customerId = db.Column(db.Integer, db.ForeignKey("customers.customerId"))  # Ensure correct table 
    vendorId = db.Column(db.Integer, db.ForeignKey("vendors.vendorId"))
    created_at = db.Column(db.DateTime,default=datetime.now())
    updated_at = db.Column(db.DateTime,onupdate=datetime.now())


def __init__(self,message,rating,feedback_date):
        super(Feedback, self).__init__()
        self.message = message
        self.rating = rating
        self.feedback_date = feedback_date
               
          

def __repr__(self):
      return f'{self.message} {self.rating}'