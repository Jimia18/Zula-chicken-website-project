from flask import Flask
from app.extensions import db,migrate


def create_app():

    app = Flask(__name__)
    app.config.from_object('config.Config')


    db.init_app(app)
    migrate.init_app(app,db)
    #jwt.init_app(app)


    #importing models
    from app.models.customer_model import Customer
    from app.models.order_model import Order
    from app.models.orderItem_model import OrderItem
    from app.models.vendor_model import Vendor
    from app.models.MenuItem_model import MenuItem
    from app.models.cart_model import CartModel
    from app.models.cartItem_model import CartItem
    from app.models.review_model import Review
    from app.models.delivery_model import Delivery
    from app.models.payment_model import Payment
    from app.models.contactMessage_model import ContactMessage


    @app.route('/')
    def home():
        return """
<html>
    <head>
        <title>Zula's Chicken</title>
        <style>
            body {
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background: linear-gradient(to right, #e0c3fc, #8ec5fc);
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
            }
            .container {
                background: white;
                padding: 40px;
                border-radius: 16px;
                box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
                text-align: center;
                max-width: 600px;
            }
            h1 {
                color: #6a0dad;
                font-size: 2em;
                margin-bottom: 20px;
            }
            p {
                font-size: 1.1em;
                color: #333;
            }
            .btn {
                margin-top: 20px;
                padding: 12px 24px;
                font-size: 1em;
                background-color: #6a0dad;
                color: white;
                border: none;
                border-radius: 8px;
                cursor: pointer;
                text-decoration: none;
            }
            .btn:hover {
                background-color: #530baf;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🎉 Welcome to Zula's Chicken </h1>
            <p></p>
            <p></p>
            <a href="#" class="btn">Please Enjoy!</a>
        </div>
    </body>
    </html>
    """


 
    
  
    
    

    return app
