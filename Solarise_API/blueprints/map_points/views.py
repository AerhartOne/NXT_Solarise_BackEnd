from flask import Blueprint, request
from flask.json import jsonify
from models.map_point import MapPoint
from models.user import User
from flask_jwt_extended import jwt_required, get_jwt_identity

map_points_api_blueprint = Blueprint('map_points_api',
                             __name__,
                             template_folder='templates')

@map_points_api_blueprint.route('/', methods=['GET'])
def index():
    return "Map Points API."

@map_points_api_blueprint.route('/new', methods=['POST'])
@jwt_required
def new():
    parent_user = User.get_or_none(User.username == get_jwt_identity())
    point_name = request.form['point_name']
    latitude = request.form['latitude']
    longitude = request.form['longitude']
    date = request.form['date']

    if (parent_user):
        created_map_point = MapPoint.create(
            parent_user=parent_user.id,
            point_name=point_name,
            latitude=latitude,
            longitude=longitude,
            date=date
        )

        return jsonify( created_map_point.as_dict() )