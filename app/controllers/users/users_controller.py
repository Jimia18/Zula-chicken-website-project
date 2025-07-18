from flask import Blueprint,request,jsonify
from status_codes import HTTP_400_BAD_REQUEST,HTTP_409_CONFLICT,HTTP_500_INTERNAL_SERVER_ERROR,HTTP_201_CREATED,HTTP_401_UNAUTHORIZED,HTTP_200_OK 
import validators
from app.models.users_model import User
from app.extensions import db,bcrypt
from flask_jwt_extended import create_access_token,create_refresh_token,jwt_required,get_jwt_identity


#user blueprint
user = Blueprint('user', __name__,url_prefix='/api/v1/user')


#user registration
@user.route('/register', methods=['POST'])
def register_user():
    data = request.json
    username = data.get('username')
    contact = data.get('contact')
    email = data.get('email')
    user_type = data.get('user_type') if 'user_type' in data else "owner"
    password = data.get('password')
    biography = data.get('biography', '') if user_type == "owner" else ''

    if not username or not contact or not password or not email:
        return jsonify({'error': 'All fields are required'}), HTTP_400_BAD_REQUEST

    if user_type == 'owner' and not biography:
        return jsonify({'Error': 'Enter your owner biography'}), HTTP_400_BAD_REQUEST

    if len(password) < 8:
        return jsonify({'Error': 'Password is too short'}), HTTP_400_BAD_REQUEST

    if not validators.email(email):
        return jsonify({'error': 'Email is invalid'}), HTTP_400_BAD_REQUEST

    if User.query.filter_by(email=email).first() is not None:
        return jsonify({"error": 'Email address in use'}), HTTP_409_CONFLICT

    if User.query.filter_by(contact=contact).first() is not None:
        return jsonify({"error": 'Contact in use'}), HTTP_409_CONFLICT

    try:
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

        new_user = User(
            username=username,
            password=hashed_password,
            email=email,
            contact=contact,
            biography=biography,
            user_type=user_type
        )

        db.session.add(new_user)
        db.session.commit()

        name = new_user.get_full_name()

        return jsonify({
            'message': f"{name} has been created successfully as a {new_user.userType}",
            'user': {
                'username': username,
                'email': email,
                'contact': contact,
                'user_type': user_type,
                'biography': biography
            }
        }), HTTP_201_CREATED

    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), HTTP_500_INTERNAL_SERVER_ERROR

    
    
    
    
#user login
@user.route('/login',methods = ['POST'])
def login():
    
    email = request.json.get('email')
    password = request.json.get('password')
    
    try:
        
        if not password or not email:
            return jsonify({'message':'Email and password are required'}),HTTP_400_BAD_REQUEST
        
        user = User.query.filter_by(email=email).first()
        
        if user:
            is_correct_password = bcrypt.check_password_hash(user.password,password)
            
            if is_correct_password:
                access_token = create_access_token(identity=user.userId)
                refresh_token = create_refresh_token(identity=user.userId)

                return jsonify({
                    'user':{
                        'id':user.userId,
                        'username':user.get_full_name(),
                        'email':user.email,
                        'access_token':access_token,
                        'refresh_token':refresh_token,
                        'user_type':user.userType
                    },
                    "Message":"You have successfully logged into your account"
                }),HTTP_200_OK
            else:
                return jsonify({'message':'Invalid password'}),HTTP_401_UNAUTHORIZED
              
        else:
            return jsonify({'message':'Invalid email address'}),HTTP_401_UNAUTHORIZED
        
    
    except Exception as e:
        return jsonify({
            'error':str(e)
        }),HTTP_500_INTERNAL_SERVER_ERROR
    

@user.route("token/refresh", methods=["POST"])
@jwt_required(refresh=True)
def refresh():
    identity = get_jwt_identity()
    access_token = create_access_token(identity=identity)
    return jsonify({'access_token':access_token})

#getting all users
@user.route('/', methods=['GET'])
def get_all_users():
    try:
        users = User.query.all()
        users_list = [{
            "userId": user.userId,
            "username": user.username,
            "email": user.email
        } for user in users]

        return jsonify({"users": users_list}), HTTP_200_OK
    except Exception as e:
        return jsonify({"error": str(e)}), 500



