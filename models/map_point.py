from models.base_model import BaseModel
from models.user import User
import peewee as pw
import re

class MapPoint(BaseModel):
    parent_user = pw.ForeignKeyField(User, backref='map_points')
    point_name = pw.CharField()
    latitude = pw.DecimalField()
    longitude = pw.DecimalField()
    date = pw.DateField()

    def as_dict(self):
        output_dict = {
            'parent_user': self.parent_user,
            'point_name': self.point_name,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'date': self.date
        }
        return output_dict