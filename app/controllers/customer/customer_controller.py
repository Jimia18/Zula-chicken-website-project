from flask import Blueprint, request, jsonify
from status_codes import HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND, HTTP_201_CREATED, HTTP_500_INTERNAL_SERVER_ERROR, HTTP_200_OK
from app.models.customer_model import Customer
from app.extensions import db, bcrypt

customer_bp = Blueprint('customer', __name__, url_prefix='/api/v1/customer')

# Create a customer
@customer_bp.route('/create', methods=['POST'])
def create_customer():
    data = request.get_json()
    customer_name = data.get('customer_name')
    email = data.get('email')
    phone_number = data.get('phone_number')
    password = data.get('password')

    # Validate fields
    if not customer_name or not email or not phone_number or not password:
        return jsonify({'error': 'All fields are required'}), HTTP_400_BAD_REQUEST

    # Check if email or phone already exists
    if Customer.query.filter_by(email=email).first():
        return jsonify({'error': 'Email already in use'}), HTTP_400_BAD_REQUEST
    if Customer.query.filter_by(phone_number=phone_number).first():
        return jsonify({'error': 'Phone number already in use'}), HTTP_400_BAD_REQUEST

    try:
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

        new_customer = Customer(
            customer_name=customer_name,
            email=email,
            phone_number=phone_number,
            password=hashed_password
        )
        db.session.add(new_customer)
        db.session.commit()

        return jsonify({'message': f'Customer {customer_name} created successfully'}), HTTP_201_CREATED

    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), HTTP_500_INTERNAL_SERVER_ERROR

# Get all customers
@customer_bp.route('/', methods=['GET'])
def get_all_customers():
    try:
        customers = Customer.query.all()
        customers_list = []
        for c in customers:
            customers_list.append({
                'customerId': c.customerId,
                'customer_name': c.customer_name,
                'email': c.email,
                'phone_number': c.phone_number,
                'created_at': c.created_at
            })

        return jsonify({
            'message': 'All customers retrieved successfully',
            'total_customers': len(customers_list),
            'customers': customers_list
        }), HTTP_200_OK

    except Exception as e:
        return jsonify({'error': str(e)}), HTTP_500_INTERNAL_SERVER_ERROR

# Get customer by ID
@customer_bp.route('/customer/<int:id>', methods=['GET'])
def get_customer_by_id(id):
    try:
        customer = Customer.query.get(id)
        if not customer:
            return jsonify({'error': 'Customer not found'}), HTTP_404_NOT_FOUND

        customer_data = {
            'customerId': customer.customerId,
            'customer_name': customer.customer_name,
            'email': customer.email,
            'phone_number': customer.phone_number,
            'created_at': customer.created_at
        }
        return jsonify({
            'message': 'Customer retrieved successfully',
            'customer': customer_data
        }), HTTP_200_OK

    except Exception as e:
        return jsonify({'error': str(e)}), HTTP_500_INTERNAL_SERVER_ERROR

# Delete a customer
@customer_bp.route('/delete/<int:id>', methods=['DELETE'])
def delete_customer(id):
    try:
        customer = Customer.query.get(id)
        if not customer:
            return jsonify({'error': 'Customer not found'}), HTTP_404_NOT_FOUND

        db.session.delete(customer)
        db.session.commit()

        return jsonify({'message': f'Customer {customer.customer_name} deleted successfully'}), HTTP_200_OK

    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), HTTP_500_INTERNAL_SERVER_ERROR
    
    # Update a customer
@customer_bp.route('/update/<int:id>', methods=['PUT'])     
def update_customer(id):
    data = request.get_json()
    customer = Customer.query.get(id)

    if not customer:
        return jsonify({'error': 'Customer not found'}), HTTP_404_NOT_FOUND

    customer_name = data.get('customer_name', customer.customer_name)
    email = data.get('email', customer.email)
    phone_number = data.get('phone_number', customer.phone_number)
    password = data.get('password')

    # Validate fields
    if not customer_name or not email or not phone_number:
        return jsonify({'error': 'All fields are required'}), HTTP_400_BAD_REQUEST

    # Check if email or phone already exists
    if Customer.query.filter(Customer.email == email, Customer.customerId != id).first():
        return jsonify({'error': 'Email already in use'}), HTTP_400_BAD_REQUEST
    if Customer.query.filter(Customer.phone_number == phone_number, Customer.customerId != id).first():
        return jsonify({'error': 'Phone number already in use'}), HTTP_400_BAD_REQUEST

    try:
        customer.customer_name = customer_name
        customer.email = email
        customer.phone_number = phone_number
        if password:
            hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
            customer.password = hashed_password

        db.session.commit()

        return jsonify({'message': f'Customer {customer_name} updated successfully'}), HTTP_200_OK

    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), HTTP_500_INTERNAL_SERVER_ERROR
