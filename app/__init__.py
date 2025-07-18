from flask import Flask
from app.extensions import db,migrate,jwt
from app.controllers.users.users_controller import user 
from app.controllers.customer.customer_controller import customer_bp
# from app.controllers.order.order_controller import order  # Uncomment if you have an order controller



def create_app():

    app = Flask(__name__)
    app.config.from_object('config.Config')


    db.init_app(app)
    migrate.init_app(app,db)
    jwt.init_app(app)


    #importing models
    from app.models.customer_model import Customer
    from app.models.order_model import Order
    from app.models.orderItem_model import OrderItem
    from app.models.users_model import User
    from app.models.MenuItem_model import MenuItem
    from app.models.cart_model import CartModel
    from app.models.cartItem_model import CartItem
    from app.models.review_model import Review
    from app.models.delivery_model import Delivery
    from app.models.payment_model import Payment
    from app.models.contactMessage_model import ContactMessage

    # Registering blueprints
    app.register_blueprint(user)
    app.register_blueprint(customer_bp)
    # app.register_blueprint(order)    

    @app.route('/')
    def home():
        return "Welcome to Zula's Backend API!"

    return app
