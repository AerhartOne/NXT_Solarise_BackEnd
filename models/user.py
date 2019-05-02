from models.base_model import BaseModel
import peewee as pw
import re

class User(BaseModel):
    username = pw.CharField(unique=True)
    email = pw.CharField()
    first_name = pw.CharField(default='J')
    last_name = pw.CharField(default='Doe')
    password = pw.TextField()

    def validate(self):
        username_valid = (User.select().where(User.username == self.username).count() == 0)
        email_valid = re.match("^.+[@].+[.].+$",str(self.email))
        password_valid = re.match(".{6}", str(self.password))
        if not email_valid:
            self.errors.append("Email has to be a valid format.")
        if not password_valid:
            self.errors.append("Password needs to be at least 6 characters long.")
        if not username_valid:
            self.errors.append("Username already exists.")

        if email_valid and password_valid and username_valid:
            return True
        else:
            return False

    

