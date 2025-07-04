from app.extensions import db  # Import db after it's initialized in __init__.py
from datetime import datetime

class MenuItem(db.Model):
    __tablename__ = "menuItems"
    menuItemId = db.Column(db.Integer,primary_key = True, nullable=False)
    item_name = db.Column(db.String(150),nullable = False)
    item_category = db.Column(db.String(150),nullable = False,unique=True)
    price = db.Column(db.Integer, nullable=False)
    description = db.Column(db.Text(),nullable = False)
    image = db.Column(db.String(225),nullable = False)
    created_at = db.Column(db.DateTime,default=datetime.now())
    updated_at = db.Column(db.DateTime,onupdate=datetime.now())

def __init__(self,item_name,item_category,description,price,image):
        super(MenuItem, self).__init__()
        self.item_name = item_name
        self.item_category = item_category
        self.description = description
        self.price = price
        self.image = image
        
          

def __repr__(self):
      return f'{self.name} {self.image}'