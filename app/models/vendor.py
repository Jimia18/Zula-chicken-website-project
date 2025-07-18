from app.extensions import db  # Import db after it's initialized in __init__.py
from datetime import datetime

class User(db.Model):
    __tablename__ = "users"
    userId = db.Column(db.Integer,primary_key = True, nullable=False)
    user_name = db.Column(db.String(150),nullable = False)
    email = db.Column(db.String(150),nullable = False,unique = True)
    phone_number = db.Column(db.String(150),nullable = False,unique=True)
    password = db.Column(db.Text(),nullable=False)
    location = db.Column(db.Text(),nullable = False)
    description = db.Column(db.Text(),nullable = False)

    # Relationships can be added here if needed  
    orders = db.relationship('Order', bac='user', lazy=True)

    created_at = db.Column(db.DateTime,default=datetime.now())
    updated_at = db.Column(db.DateTime,onupdate=datetime.now())

def __init__(self,user_name,email,phone_number,password,location,description):
        super(User, self).__init__()
        self.user_name = user_name
        self.email = email
        self.phone_number = phone_number
        self.password = password
        self.location = location
        self.description = description
          

def __repr__(self):
      return f'{self.name} {self.location}'