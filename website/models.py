from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


# Note Schema
class Note(db.Model):
    id = db.Column(db.Integer, primary_key = True) # id is autocreated and incrememted
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone = True), default = func.now()) # No need to set time, uses the time zone and calls func.now to grab it
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) # Foreign Key to match the corresponding User (1 to many relationship).
        # Note: For foreign key 'user.id' is lowercase


# User Schema
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True) # Unqiue integer value
    email = db.Column(db.String(150), unique = True) # Max string length is 150, No user can have the same email
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note') # Store list of all the notes that the user has created
        # Note: When calling relationship, 'Note' is uppercase
