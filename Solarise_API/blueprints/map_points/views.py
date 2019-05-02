from flask import Blueprint

map_points_api_blueprint = Blueprint('map_points_api',
                             __name__,
                             template_folder='templates')

@map_points_api_blueprint.route('/', methods=['GET'])
def index():
    return "Map Points API."
