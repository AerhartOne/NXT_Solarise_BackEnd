from flask import Blueprint, request
from flask.json import jsonify
from models.map_point import MapPoint

map_points_api_blueprint = Blueprint('map_points_api',
                             __name__,
                             template_folder='templates')

@map_points_api_blueprint.route('/', methods=['GET'])
def index():
    return "Map Points API."

@map_points_api_blueprint.route('/new', methods=['GET'])
def new():
    parent_user = request.form['parent_user']
    point_name = request.form['point_name']
    latitude = request.form['latitude']
    longitude = request.form['longitude']
    date = request.form['date']

    created_map_point = MapPoint.create(
        parent_user=parent_user,
        point_name=point_name,
        latitude=latitude,
        longitude=longitude,
        date=date
    )

    return jsonify( created_map_point.as_dict() )