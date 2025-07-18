
from app.extensions import db
from datetime import datetime
class User(db.Model):
    __tablename__="users"
    userId = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(50),nullable=False)
    email = db.Column(db.String(100),nullable=False,unique=True)
    contact = db.Column(db.String(50),nullable=False,unique=True)
    image = db.Column(db.String(255),nullable=True)
    password = db.Column(db.Text(),nullable=False)
    biography = db.Column(db.Text, nullable=False)
    userType = db.Column(db.String(20), nullable=True)  # e.g., 'admin', 'user', etc.
    createdAt = db.Column(db.DateTime,default=datetime.now())
    updatedAt = db.Column(db.DateTime,onupdate=datetime.now())

    def __init__(self,username,email,contact,password,biography,user_type,image=None):
        super(User, self).__init__()
        self.username = username
        self.email = email
        self.contact = contact
        self.password = password
        self.biography = biography
        self.userType = user_type
        self.image = image
    

    def get_full_name(self):
        return f'{self.username}'
