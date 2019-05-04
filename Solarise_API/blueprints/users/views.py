from flask import Blueprint, request
from flask.json import jsonify
from models.user import User
from models.map_point import MapPoint
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, create_refresh_token, get_jwt_identity, jwt_required

users_api_blueprint = Blueprint('users_api',
                             __name__,
                             template_folder='templates')

@users_api_blueprint.route('/', methods=['GET'])
def index():
    return "USERS API"

@users_api_blueprint.route('/new', methods=['POST'])
def new():
    data = request.form
    username = data['username']
    email = data['email']
    hashed_password = generate_password_hash( data['password'] )
    first_name = data['first_name']
    last_name = data['last_name']
    new_user = None

    if User.get_or_none(User.username == username) == None:
        new_user = User.create(
            username=username,
            email=email,
            password=hashed_password,
            first_name=first_name,
            last_name=last_name 
        )

    return jsonify( new_user.as_dict() )

@users_api_blueprint.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    if username and password:
        target_user = User.get_or_none(User.username == username)

        if target_user and check_password_hash(target_user.password, password):
            access_token = create_access_token(identity=username)
            refresh_token = create_refresh_token(identity=username)
            return_data = {
                'access_token': access_token,
                'refresh_token': refresh_token,
                'userdata': target_user.as_dict()
            }
            return jsonify(return_data), 200
        else:
            return jsonify( {'msg': f'Invalid password.'}), 403

    else:
        return jsonify( {'msg': f'Invalid username or password.'}), 500

@users_api_blueprint.route('/self', methods=['GET'])
@jwt_required
def own_data():
    selected_user = User.get_or_none(User.username == get_jwt_identity())
    if selected_user:
        return jsonify( selected_user.as_dict() ), 200
    else:
        return jsonify( {'msg': 'Could not find user.'} ), 404

@users_api_blueprint.route('/self/map_points', methods=['GET'])
@jwt_required
def saved_points():
    selected_user = User.get_or_none(User.username == get_jwt_identity())
    output = []
    if selected_user:
        selectedPoints = MapPoint.select().where(MapPoint.parent_user == selected_user)
        output = [map_point.as_dict() for map_point in selectedPoints]
    
    return jsonify( output )

@users_api_blueprint.route('/self/edit', methods=['POST'])
@jwt_required
def edit():
    selected_user = User.get_or_none(User.username == get_jwt_identity())
    data = request.form

    if selected_user:
        User.update(
            email=data['email'],
            first_name=data['first_name'],
            last_name=data['last_name']
        ).where(User.id == selected_user.id).execute()
        if data['password'] != '':
            User.update( password = generate_password_hash(data['password'])
            ).where(User.id == selected_user.id).execute()
        return jsonify( selected_user.as_dict() )
    else:
        return jsonify( {'msg': 'Could not find user.'} ), 404
