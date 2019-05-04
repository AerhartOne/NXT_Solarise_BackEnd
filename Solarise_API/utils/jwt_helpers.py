import os
from app import app
from flask_jwt_extended import JWTManager

app.config['JWT_SECRET_KEY'] = b'\xef\x021\x19x\x90\xb7\x93\xa0\xd9+\xee\x89\xd7s\x04\x90n\x93\x1e\xb82\xfbA\xde\xd7\xcc\xbcl:\xfa{'
jwt = JWTManager(app)